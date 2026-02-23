# Smart CCTV System - Project Summary

## 📋 Overview

A complete, production-ready intelligent CCTV surveillance system with motion detection, video recording, alert management, and a professional web dashboard.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Webcam or IP camera
- Modern web browser

### Installation

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup configuration
python setup.py

# 3. Edit .env with your camera settings
# (Optional - system works with defaults)

# 4. Run the system
python main.py

# 5. Open dashboard
# http://localhost:5000
```

## 📁 Complete Project Structure

```
SMART CCTV/
├── .github/
│   └── copilot-instructions.md    # Project guidelines
├── .vscode/
│   ├── launch.json                # Debug configuration
│   └── tasks.json                 # VS Code tasks
├── config/
│   └── config.yaml                # System configuration
├── logs/                          # Application logs
├── recordings/                    # Video storage
├── src/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── server.py              # Flask REST API
│   ├── alerts/
│   │   ├── __init__.py
│   │   └── alert_manager.py       # Alert system
│   ├── camera/
│   │   ├── __init__.py
│   │   ├── capture.py             # Camera capture
│   │   ├── frame_converter.py     # Frame processing
│   │   └── recorder.py            # Video recording
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py              # Database models
│   │   └── manager.py             # Database operations
│   └── motion_detection/
│       ├── __init__.py
│       └── detector.py            # Motion detector
├── tests/
│   ├── test_alert_manager.py      # Alert tests
│   └── test_motion_detector.py    # Motion tests
├── web/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css          # Dashboard styles
│   │   └── js/
│   │       └── main.js            # Dashboard logic
│   └── templates/
│       └── index.html             # Web interface
├── .env.example                   # Environment template
├── .gitignore                     # Git ignore rules
├── main.py                        # Application entry point
├── README.md                      # Full documentation
├── requirements.txt               # Python dependencies
└── setup.py                       # Setup script
```

## 🎯 Core Features

### 1. Camera System (`src/camera/`)
- **CameraCapture**: Real-time video capture from webcams/IP cameras
- **FrameConverter**: Image processing and optimization
- **VideoRecorder**: Automatic video recording with quality control
- Configurable resolution and FPS
- Frame queue for processing

### 2. Motion Detection (`src/motion_detection/`)
- **MotionDetector**: Advanced motion detection algorithm
- Configurable sensitivity (0.1-0.9)
- Minimum area threshold to filter noise
- Contour detection and visualization
- Real-time motion analytics

### 3. Alert System (`src/alerts/`)
- **AlertManager**: Multi-channel alert delivery
- Webhook support for integrations
- Cooldown period to prevent alert spam
- Alert history tracking
- Multiple alert types (motion, system, error)

### 4. Database (`src/database/`)
- **Models**: Complete ORM models for:
  - Cameras
  - Recordings
  - Events
  - Alerts
  - System Logs
- **Manager**: CRUD operations and queries
- SQLite database (file-based, no server needed)
- Automatic table creation

### 5. REST API (`src/api/`)
- **APIServer**: Flask-based REST API
- Endpoints for cameras, recordings, events, alerts
- JSON responses
- CORS support for web integration
- Health check endpoint

### 6. Web Dashboard
- Professional UI with responsive design
- Real-time statistics
- Camera management
- Recording browsing
- Event logging
- Alert history
- Configuration panel
- Mobile-friendly interface

## 🔧 Configuration

### Environment Variables (.env)

```
# Server
FLASK_APP=main.py
FLASK_ENV=development
FLASK_PORT=5000
DEBUG=True

# Camera
CAMERA_ID=0
CAMERA_FPS=30
CAMERA_WIDTH=1280
CAMERA_HEIGHT=720

# Motion Detection
MOTION_SENSITIVITY=0.3
MOTION_MIN_AREA=500

# Recording
RECORDING_ENABLED=True
RECORDING_FORMAT=mp4

# Alerts
ALERT_ENABLED=True
WEBHOOK_URL=http://localhost:8000/alert
ALERT_COOLDOWN=60

# Database
DATABASE_URL=sqlite:///./data/cctv.db
```

## 🌐 API Endpoints

```
GET  /api/health              - System health status
GET  /api/cameras             - List all cameras
GET  /api/cameras/<id>        - Camera details
GET  /api/recordings          - Video recordings
GET  /api/events              - Event log
GET  /api/alerts              - Alert history
GET  /                        - Web dashboard
```

## 💡 Key Components

### CameraCapture
```python
camera = CameraCapture(camera_id=0, fps=30, width=1280, height=720)
camera.start()
frame = camera.get_frame()
camera.stop()
```

### MotionDetector
```python
detector = MotionDetector(sensitivity=0.3, min_area=500)
motion_detected, contours = detector.detect(frame)
if motion_detected:
    frame = detector.draw_contours(frame)
```

### AlertManager
```python
alert_manager = AlertManager(webhook_url="http://webhook.url", 
                            cooldown_period=60)
alert_manager.trigger_alert(AlertType.MOTION, "Motion detected")
history = alert_manager.get_alert_history()
```

### DatabaseManager
```python
db_manager = DatabaseManager(app)
db_manager.create_tables()
camera = db_manager.add_camera("Front Door", 0)
recordings = db_manager.get_recordings(limit=50)
```

## 🧪 Testing

### Run Unit Tests
```bash
python -m pytest tests/ -v
```

### Test Files
- `tests/test_motion_detector.py` - Motion detection tests
- `tests/test_alert_manager.py` - Alert system tests

## 📊 Monitoring

The system logs all activities to:
- Console output (real-time)
- `logs/cctv.log` (file storage)

Adjust logging level in `.env`:
- DEBUG: Detailed diagnostics
- INFO: General information
- WARNING: Warning messages
- ERROR: Error messages

## 🔐 Security Features

- Environment-based configuration (no hardcoded secrets)
- Database queries use ORM (SQL injection safe)
- CORS restrictions for API
- Webhook signature validation ready
- Alert cooldown to prevent DoS

## 📈 Performance Tips

1. **Resolution**: Reduce camera resolution for faster processing
   ```
   CAMERA_WIDTH=640
   CAMERA_HEIGHT=480
   ```

2. **Motion Sensitivity**: Tune to reduce false positives
   ```
   MOTION_SENSITIVITY=0.4
   MOTION_MIN_AREA=1000
   ```

3. **Recording**: Disable if not needed
   ```
   RECORDING_ENABLED=False
   ```

4. **FPS**: Lower FPS for better performance
   ```
   CAMERA_FPS=15
   ```

## 🛠️ Development

### Project Setup
```bash
python setup.py
```

### Run with Debug
```bash
set FLASK_ENV=development
python main.py
```

### VS Code Tasks
- `Ctrl+Shift+B` - Run Smart CCTV System
- View Tasks - Install Dependencies
- View Tasks - Run Tests

## 📚 File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Application entry point, orchestrates all systems |
| `setup.py` | Initial project setup and configuration |
| `requirements.txt` | Python package dependencies |
| `config/config.yaml` | Detailed configuration options |
| `src/camera/capture.py` | Video capture and streaming |
| `src/motion_detection/detector.py` | Motion detection engine |
| `src/alerts/alert_manager.py` | Alert triggering and delivery |
| `src/database/models.py` | SQLAlchemy database models |
| `src/database/manager.py` | Database CRUD operations |
| `src/api/server.py` | Flask REST API server |
| `web/templates/index.html` | Web dashboard HTML |
| `web/static/css/style.css` | Dashboard styling |
| `web/static/js/main.js` | Dashboard JavaScript |

## 🚨 Troubleshooting

### Camera Not Working
- Check `CAMERA_ID` in .env (use 0 for default)
- Verify camera permissions
- Test with: `python -c "import cv2; print(cv2.VideoCapture(0).isOpened())"`

### Motion Not Detected
- Adjust `MOTION_SENSITIVITY` (lower = more sensitive)
- Increase `MOTION_MIN_AREA` to reduce false positives
- Check lighting conditions

### Database Errors
- Delete `data/cctv.db` to reset
- Run: `python -c "from src.database.models import db; db.create_all()"`

### Port Already in Use
- Change `FLASK_PORT` in .env
- Or kill process: `netstat -ano | findstr :5000`

## 📝 License

Educational and personal use project.

## 📞 Support

For issues or questions, check:
1. README.md - Detailed documentation
2. Console logs - Error messages
3. logs/cctv.log - Application log

## 🎓 Learning Resources

This project demonstrates:
- Python video processing with OpenCV
- Flask REST API development
- SQLAlchemy ORM
- Responsive web design
- Real-time event handling
- System architecture patterns
- Threading and async operations
- Database management

---

**Version**: 1.0.0  
**Last Updated**: November 2025
