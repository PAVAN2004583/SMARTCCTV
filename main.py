import os
import sys
import logging
from dotenv import load_dotenv
import cv2
import webbrowser
import time

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/cctv.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

from api.server import APIServer
from camera.capture import CameraCapture
from motion_detection.detector import MotionDetector
from alerts.alert_manager import AlertManager, AlertType
from camera.recorder import VideoRecorder
from database.manager import DatabaseManager
from database.models import db


class SmartCCTVSystem:
    """Main Smart CCTV System class."""
    
    def __init__(self):
        self.camera_capture = None
        self.motion_detector = None
        self.alert_manager = None
        self.video_recorder = None
        self.db_manager = None
        self.api_server = None
        self.is_running = False
        
        logger.info("Smart CCTV System initialized")
    
    def setup(self):
        """Setup all system components."""
        logger.info("Setting up Smart CCTV System components...")
        
        # Initialize camera
        camera_id = int(os.getenv('CAMERA_ID', 0))
        camera_fps = int(os.getenv('CAMERA_FPS', 30))
        camera_width = int(os.getenv('CAMERA_WIDTH', 1280))
        camera_height = int(os.getenv('CAMERA_HEIGHT', 720))
        
        self.camera_capture = CameraCapture(
            camera_id=camera_id,
            fps=camera_fps,
            width=camera_width,
            height=camera_height
        )
        
        # Initialize motion detector
        motion_sensitivity = float(os.getenv('MOTION_SENSITIVITY', 0.3))
        motion_min_area = int(os.getenv('MOTION_MIN_AREA', 500))
        
        self.motion_detector = MotionDetector(
            sensitivity=motion_sensitivity,
            min_area=motion_min_area
        )
        
        # Initialize alert manager
        webhook_url = os.getenv('WEBHOOK_URL')
        alert_cooldown = int(os.getenv('ALERT_COOLDOWN', 60))
        
        self.alert_manager = AlertManager(
            webhook_url=webhook_url,
            cooldown_period=alert_cooldown
        )
        
        # Initialize video recorder
        recording_enabled = os.getenv('RECORDING_ENABLED', 'True') == 'True'
        if recording_enabled:
            recordings_dir = os.path.join(os.path.dirname(__file__), 'recordings')
            os.makedirs(recordings_dir, exist_ok=True)
            self.video_recorder = VideoRecorder(
                output_dir=recordings_dir,
                fps=camera_fps,
                width=camera_width,
                height=camera_height
            )

        # Initialize snapshots directory for motion snapshots
        snapshots_dir = os.path.join(os.path.dirname(__file__), 'snapshots')
        os.makedirs(snapshots_dir, exist_ok=True)
        self.snapshots_dir = snapshots_dir
        
        # Initialize database
        self.db_manager = DatabaseManager()
        
        # Initialize API server
        self.api_server = APIServer()
        
        logger.info("Smart CCTV System setup complete")
    
    def start_flask_app(self):
        """Start Flask API server."""
        logger.info("Starting Flask API server...")
        app = self.api_server.get_app()
        # Attach camera and recorder instances to app config so routes can access them
        app.config['camera_capture'] = self.camera_capture
        app.config['video_recorder'] = self.video_recorder
        app.config['snapshots_dir'] = getattr(self, 'snapshots_dir', None)

        # Initialize database with app
        self.db_manager.init_app(app)
        with app.app_context():
            db.create_all()
        
        port = int(os.getenv('FLASK_PORT', 5000))
        debug = os.getenv('DEBUG', 'False') == 'True'
        
        app.run(host='0.0.0.0', port=port, debug=debug, use_reloader=False)
    
    def run(self):
        """Run the Smart CCTV System."""
        try:
            self.setup()
            
            # Start camera capture
            if not self.camera_capture.start():
                logger.error("Failed to start camera capture")
                return
            
            # Start recording if enabled
            if self.video_recorder:
                self.video_recorder.start_recording()
            
            self.is_running = True
            logger.info("Smart CCTV System is now running")
            
            # Start Flask app in separate thread
            import threading
            flask_thread = threading.Thread(target=self.start_flask_app, daemon=True)
            flask_thread.start()

            # Try to open the web UI in the default browser shortly after server starts
            try:
                port = int(os.getenv('FLASK_PORT', 5000))
                # give the server a moment to bind
                time.sleep(1.0)
                url = f'http://localhost:{port}/'
                webbrowser.open(url)
                logger.info(f'Opened web UI at {url}')
            except Exception:
                logger.warning('Failed to open web UI automatically')
            
            # Main processing loop
            self._process_frames()
            
        except KeyboardInterrupt:
            logger.info("Keyboard interrupt received")
            self.shutdown()
        except Exception as e:
            logger.error(f"Error running system: {str(e)}")
            self.shutdown()
    
    def _process_frames(self):
        """Process frames from camera."""
        while self.is_running:
            try:
                frame = self.camera_capture.get_frame()
                
                if frame is None:
                    continue
                
                # Detect motion
                motion_detected, contours = self.motion_detector.detect(frame)
                
                # Draw contours if motion detected
                if motion_detected:
                    frame = self.motion_detector.draw_contours(frame)
                    
                    # Trigger alert
                    motion_info = self.motion_detector.get_motion_info()

                    # Save snapshot image
                    try:
                        import time as time_module
                        ts = int(time_module.time())
                        filename = f"snapshot_{ts}.jpg"
                        snapshot_path = os.path.join(self.snapshots_dir, filename)
                        cv2.imwrite(snapshot_path, frame)
                    except Exception as e:
                        logger.error(f"Failed to write snapshot: {e}")

                    self.alert_manager.trigger_alert(
                        AlertType.MOTION,
                        f"Motion detected with {len(contours)} regions",
                        motion_info,
                        app=self.api_server.get_app()
                    )
                
                # Record frame
                if self.video_recorder and self.video_recorder.is_recording:
                    self.video_recorder.write_frame(frame)
                
            except Exception as e:
                logger.error(f"Error processing frame: {str(e)}")
                continue
    
    def shutdown(self):
        """Shutdown the system."""
        logger.info("Shutting down Smart CCTV System...")
        self.is_running = False
        
        if self.camera_capture:
            self.camera_capture.stop()
        
        if self.video_recorder:
            self.video_recorder.stop_recording()
        
        logger.info("Smart CCTV System shutdown complete")


def main():
    """Main entry point."""
    system = SmartCCTVSystem()
    system.run()


if __name__ == '__main__':
    main()
