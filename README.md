# Smart CCTV System

A comprehensive intelligent CCTV surveillance system with motion detection, recording, alerts, and web dashboard.

## Features

- **Real-time Camera Capture**: Connect and manage multiple camera streams
- **Motion Detection**: Advanced motion detection with configurable sensitivity
- **Video Recording**: Automatic video recording with quality control
- **Alert System**: Email and webhook alerts for motion events
- **Web Dashboard**: Professional web interface for monitoring
- **Database Management**: SQLite database for recordings and events
- **REST API**: Complete API for integration and automation
- **Event Logging**: Comprehensive event and alert history

## Project Structure

```
├── src/
│   ├── camera/           # Camera capture and streaming
│   │   ├── capture.py   # Camera capture module
│   │   ├── frame_converter.py  # Frame processing
│   │   └── recorder.py  # Video recording
│   ├── motion_detection/ # Motion detection algorithms
│   │   └── detector.py  # Motion detector
│   ├── alerts/          # Alert system
│   │   └── alert_manager.py  # Alert management
│   ├── database/        # Database operations
│   │   ├── models.py   # Database models
│   │   └── manager.py  # Database manager
│   └── api/             # REST API
│       └── server.py   # Flask API server
├── web/                 # Web dashboard
│   ├── templates/      # HTML templates
│   │   └── index.html
│   └── static/         # CSS and JavaScript
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── config/             # Configuration files
│   └── config.yaml
├── recordings/         # Video recording storage
├── logs/              # Application logs
├── tests/             # Unit tests
├── main.py           # Application entry point
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variables example
└── README.md         # This file
```

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Webcam or IP camera for video input

### Steps

1. Clone or download this project

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create environment configuration:
   ```bash
   cp .env.example .env
   ```

4. Edit `.env` file with your settings:
   ```
   FLASK_APP=main.py
   FLASK_ENV=development
   CAMERA_ID=0
   CAMERA_FPS=30
   CAMERA_WIDTH=1280
   CAMERA_HEIGHT=720
   MOTION_SENSITIVITY=0.3
   MOTION_MIN_AREA=500
   RECORDING_ENABLED=True
   DEBUG=True
   ```

5. Initialize the database:
   ```bash
   python -m src.database.init
   ```

## Running the Application

### Start the system:
```bash
python main.py
```

The application will:
- Initialize all components
- Start camera capture
- Begin motion detection
- Start recording
- Launch the web dashboard at `http://localhost:5000`

### Access the Dashboard

Open your web browser and go to:
```
http://localhost:5000
```

## Configuration

### Camera Settings

Edit `.env` file:
- `CAMERA_ID`: Camera device ID (default: 0)
- `CAMERA_FPS`: Frames per second (default: 30)
- `CAMERA_WIDTH`: Resolution width (default: 1280)
- `CAMERA_HEIGHT`: Resolution height (default: 720)

### Motion Detection

- `MOTION_SENSITIVITY`: Sensitivity level 0.1-0.9 (default: 0.3)
- `MOTION_MIN_AREA`: Minimum motion area in pixels (default: 500)

### Recording

- `RECORDING_ENABLED`: Enable/disable video recording (default: True)
- Recording quality can be adjusted in settings

### Alerts

- `ALERT_ENABLED`: Enable/disable alerts (default: True)
- `WEBHOOK_URL`: Webhook endpoint for motion alerts
- `ALERT_COOLDOWN`: Cooldown period between alerts in seconds (default: 60)

## API Endpoints

### Health Check
- `GET /api/health` - System health status

### Cameras
- `GET /api/cameras` - Get all cameras
- `GET /api/cameras/<id>` - Get camera details

### Recordings
- `GET /api/recordings` - Get video recordings

### Events
- `GET /api/events` - Get event log

### Alerts
- `GET /api/alerts` - Get alert history

## Dashboard Features

### Overview
- System status and statistics
- Active cameras count
- Recent recordings and events
- Alert history

### Cameras
- View all connected cameras
- Camera status and location
- Real-time monitoring

### Recordings
- Browse video recordings
- View file size and duration
- Automatic cleanup of old files

### Events
- Motion detection events
- System events and errors
- Event filtering and search

### Alerts
- Alert history
- Alert status tracking
- Alert management

### Settings
- Camera configuration
- Motion detection tuning
- Recording quality settings

## Troubleshooting

### Camera not detected
- Check camera ID in `.env` (usually 0 for default camera)
- Ensure camera is properly connected
- Check camera permissions

### Motion detection not working
- Adjust sensitivity value (0.1 = very sensitive, 0.9 = less sensitive)
- Increase minimum area threshold if too many false positives

### Recording issues
- Ensure `recordings/` directory exists and is writable
- Check disk space availability
- Verify recording format is supported

### Web dashboard not loading
- Check if Flask server is running
- Verify port 5000 is not in use
- Check browser console for JavaScript errors

## Performance Optimization

- Adjust camera resolution for better performance
- Tune motion detection sensitivity to reduce false positives
- Enable/disable recording based on requirements
- Set appropriate cooldown period for alerts

## Security Considerations

- Change `SECRET_KEY` in `.env` for production
- Implement authentication for dashboard access
- Secure webhook endpoints
- Use HTTPS in production environments
- Restrict camera access to authorized networks

## Future Enhancements

- Multi-camera support
- Email and SMS alerts
- Cloud storage integration
- Advanced analytics and reporting
- Mobile application
- Face recognition
- Object detection
- Machine learning-based anomaly detection

## License

This project is provided as-is for educational and personal use.

## Support

For issues, questions, or improvements, please refer to the project documentation or contact the development team.

## Version

**Smart CCTV System v1.0.0**

Last Updated: 2025
