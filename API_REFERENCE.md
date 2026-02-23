# Technical Reference - Smart CCTV System

## API Documentation

### Base URL
```
http://localhost:5000/api
```

### Authentication
All requests (except `/auth/login` and `/auth/register`) require an active session.

**Headers Required:**
```
Content-Type: application/json
Cookie: session=<session_cookie>
```

---

## Authentication Endpoints

### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
  "username": "admin",
  "password": "securepassword"
}
```

**Response (201):**
```json
{
  "success": true,
  "user": {
    "id": 1,
    "username": "admin",
    "is_admin": true
  }
}
```

### Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "securepassword"
}
```

**Response (200):**
```json
{
  "success": true,
  "user": {
    "id": 1,
    "username": "admin",
    "is_admin": true
  }
}
```

### Get Current User
```http
GET /api/auth/me
```

**Response (200):**
```json
{
  "user": {
    "id": 1,
    "username": "admin",
    "is_admin": true
  }
}
```

**Response (401) if not authenticated:**
```json
{
  "error": "Not authenticated"
}
```

### Logout
```http
POST /api/auth/logout
```

**Response (200):**
```json
{
  "success": true
}
```

---

## Camera Endpoints

### List Cameras
```http
GET /api/cameras
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Front Door",
    "source": 0,
    "width": 640,
    "height": 480,
    "created_at": "2025-11-27T10:30:00"
  }
]
```

### Add Camera
```http
POST /api/cameras
Content-Type: application/json

{
  "name": "Back Yard",
  "source": 1,
  "width": 640,
  "height": 480
}
```

**Response (201):**
```json
{
  "id": 2,
  "name": "Back Yard",
  "source": 1,
  "width": 640,
  "height": 480
}
```

### Delete Camera
```http
DELETE /api/cameras/1
```

**Response:**
```json
{
  "success": true
}
```

### Get Video Stream (MJPEG)
```http
GET /api/stream
```

Returns MJPEG stream for use in `<img>` tag:
```html
<img src="/api/stream" alt="Live Stream">
```

---

## Recording Endpoints

### List Recordings
```http
GET /api/recordings
```

**Response:**
```json
[
  {
    "id": 1,
    "filename": "recording_20251127_103045.mp4",
    "file_path": "recordings/recording_20251127_103045.mp4",
    "duration": 45.5,
    "file_size": 5242880,
    "created_at": "2025-11-27T10:30:45"
  }
]
```

### Start Recording
```http
POST /api/recordings/start
```

**Response:**
```json
{
  "success": true,
  "message": "Recording started"
}
```

### Stop Recording
```http
POST /api/recordings/stop
```

**Response:**
```json
{
  "success": true,
  "filename": "recording_20251127_103045.mp4"
}
```

### Delete Recording
```http
POST /api/recordings/delete
Content-Type: application/json

{
  "file": "recording_20251127_103045.mp4"
}
```

**Response:**
```json
{
  "success": true
}
```

---

## Photo Endpoints

### List Photos
```http
GET /api/photos
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "snapshot_20251127_103030.jpg",
    "path": "snapshots/snapshot_20251127_103030.jpg",
    "created_at": "2025-11-27T10:30:30"
  }
]
```

### Delete Photo
```http
POST /api/photos/delete
Content-Type: application/json

{
  "file": "snapshot_20251127_103030.jpg"
}
```

**Response:**
```json
{
  "success": true
}
```

### Download File
```http
GET /api/download/<path>
```

Example:
```
GET /api/download/recordings/video.mp4
```

---

## Event Endpoints

### List Events
```http
GET /api/events
```

**Response:**
```json
[
  {
    "id": 1,
    "event_type": "motion",
    "camera_id": 1,
    "details": "Motion detected in frame",
    "created_at": "2025-11-27T10:30:00"
  }
]
```

### Clear Events
```http
POST /api/events/clear
```

**Response:**
```json
{
  "success": true,
  "cleared": 42
}
```

---

## Alert Endpoints

### List Alerts
```http
GET /api/alerts
```

**Response:**
```json
[
  {
    "id": 1,
    "alert_type": "motion",
    "message": "Motion detected - High severity",
    "created_at": "2025-11-27T10:30:00"
  }
]
```

### Clear Alerts
```http
POST /api/alerts/clear
```

**Response:**
```json
{
  "success": true,
  "cleared": 5
}
```

---

## Email Recipient Endpoints

### List Email Recipients
```http
GET /api/email-recipients
```

**Response:**
```json
[
  {
    "id": 1,
    "email": "admin@example.com",
    "enabled": true
  },
  {
    "id": 2,
    "email": "security@example.com",
    "enabled": false
  }
]
```

### Add Email Recipient
```http
POST /api/email-recipients
Content-Type: application/json

{
  "email": "newuser@example.com"
}
```

**Response (201):**
```json
{
  "id": 3,
  "email": "newuser@example.com",
  "enabled": true
}
```

### Delete Email Recipient
```http
DELETE /api/email-recipients/1
```

**Response:**
```json
{
  "success": true
}
```

### Toggle Email Recipient
```http
POST /api/email-recipients/1/toggle
```

**Response:**
```json
{
  "enabled": false
}
```

---

## Motion Tracking Endpoints

### Get Motion Tracking Data
```http
GET /api/motion/tracking?limit=100
```

**Query Parameters:**
- `limit` (optional): Number of records to return (default: 100)

**Response:**
```json
[
  {
    "id": 1,
    "camera_id": 1,
    "contour_count": 5,
    "motion_area_percent": 0.15,
    "severity": "high",
    "created_at": "2025-11-27T10:30:00"
  },
  {
    "id": 2,
    "camera_id": 1,
    "contour_count": 2,
    "motion_area_percent": 0.08,
    "severity": "low",
    "created_at": "2025-11-27T10:29:45"
  }
]
```

### Get Motion Statistics
```http
GET /api/motion/stats?hours=24
```

**Query Parameters:**
- `hours` (optional): Time period for statistics (default: 24)

**Response:**
```json
{
  "total_events": 42,
  "high_severity": 5,
  "medium_severity": 12,
  "low_severity": 25,
  "period_hours": 24
}
```

---

## Settings Endpoints

### Get All Settings
```http
GET /api/settings
```

**Response:**
```json
{
  "smtpServer": "smtp.gmail.com",
  "smtpPort": "587",
  "smtpUser": "admin@gmail.com",
  "motionSensitivity": "50",
  "recordingEnabled": "true",
  "retentionDays": "30"
}
```

### Save Settings
```http
POST /api/settings
Content-Type: application/json

{
  "smtpServer": "smtp.gmail.com",
  "smtpPort": "587",
  "smtpUser": "admin@gmail.com",
  "smtpPass": "app-password-here",
  "motionSensitivity": "60",
  "retentionDays": "14"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Settings saved"
}
```

---

## Database Management Endpoints

### Optimize Database
```http
POST /api/database/optimize
```

**Response:**
```json
{
  "success": true,
  "message": "Database optimized"
}
```

### Backup Database
```http
POST /api/database/backup
```

**Response:**
```json
{
  "success": true,
  "message": "Database backed up to cctv_backup_20251127_103045.db"
}
```

### Clear All Data
```http
POST /api/database/clear
```

**Response:**
```json
{
  "success": true,
  "message": "All data cleared"
}
```

---

## Database Models

### User
```python
{
  "id": Integer (Primary Key),
  "username": String(80, unique=True),
  "password_hash": String(255),
  "is_admin": Boolean (default=True),
  "created_at": DateTime
}
```

### Camera
```python
{
  "id": Integer (Primary Key),
  "name": String(100),
  "source": String(255),  # 0, 1, or file path
  "width": Integer (default=640),
  "height": Integer (default=480),
  "created_at": DateTime
}
```

### Recording
```python
{
  "id": Integer (Primary Key),
  "camera_id": Integer (Foreign Key),
  "filename": String(255),
  "file_path": String(255),
  "duration": Float,
  "file_size": Integer,
  "created_at": DateTime
}
```

### Event
```python
{
  "id": Integer (Primary Key),
  "event_type": String(50),
  "camera_id": Integer (Foreign Key),
  "details": Text,
  "created_at": DateTime
}
```

### Alert
```python
{
  "id": Integer (Primary Key),
  "alert_type": String(50),
  "message": Text,
  "created_at": DateTime
}
```

### EmailRecipient
```python
{
  "id": Integer (Primary Key),
  "email": String(255, unique=True),
  "enabled": Boolean (default=True),
  "created_at": DateTime
}
```

### MotionTracking
```python
{
  "id": Integer (Primary Key),
  "camera_id": Integer (Foreign Key),
  "contour_count": Integer,
  "motion_area_percent": Float,
  "severity": String(20),  # "low", "medium", "high"
  "created_at": DateTime
}
```

### SystemSetting
```python
{
  "id": Integer (Primary Key),
  "key": String(255, unique=True),
  "value": Text,
  "created_at": DateTime
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid request payload"
}
```

### 401 Unauthorized
```json
{
  "error": "Not authenticated"
}
```

### 403 Forbidden
```json
{
  "error": "Access denied"
}
```

### 404 Not Found
```json
{
  "error": "Not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error"
}
```

---

## JavaScript Functions

### API Calls
```javascript
// Login
await fetch('/api/auth/login', {
  method: 'POST',
  credentials: 'same-origin',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ username, password })
})

// Get motion stats
const resp = await fetch('/api/motion/stats', { 
  credentials: 'same-origin' 
})
const stats = await resp.json()

// Add email recipient
await fetch('/api/email-recipients', {
  method: 'POST',
  credentials: 'same-origin',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email })
})
```

### UI Updates
```javascript
// Load email recipients
loadEmailRecipients()  // Fetches and displays list

// Load motion tracking
loadMotionTracking()   // Shows recent motion events

// Load motion stats
loadMotionStats()      // Shows severity statistics

// Check auth status
checkAndEnforceLogin() // Redirects if not authenticated
```

---

## Configuration File

`config/config.yaml`:
```yaml
database:
  type: sqlite
  path: data/cctv.db

camera:
  default_width: 640
  default_height: 480
  fps: 30

motion_detection:
  threshold: 30
  min_contour_area: 500

server:
  host: 0.0.0.0
  port: 5000
  debug: false

logging:
  level: INFO
  file: logs/system.log
```

---

## Common HTTP Headers

### Request Headers
```
Content-Type: application/json
Accept: application/json
Cookie: session=<session_id>
Authorization: Bearer <token> (not used, sessions instead)
```

### Response Headers
```
Content-Type: application/json
Set-Cookie: session=<session_id>; Path=/; HttpOnly
X-Content-Type-Options: nosniff
```

---

## Development Tips

### Testing Endpoints with curl
```bash
# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}' \
  -c cookies.txt

# Get current user
curl http://localhost:5000/api/auth/me \
  -b cookies.txt

# Get motion stats
curl http://localhost:5000/api/motion/stats \
  -b cookies.txt
```

### Testing with Python
```python
import requests

session = requests.Session()

# Login
resp = session.post('http://localhost:5000/api/auth/login', json={
    'username': 'admin',
    'password': 'admin123'
})

# Get motion stats
resp = session.get('http://localhost:5000/api/motion/stats')
stats = resp.json()
print(stats)
```

### Browser Console Testing
```javascript
// From browser console on dashboard page
fetch('/api/motion/stats', { credentials: 'same-origin' })
  .then(r => r.json())
  .then(d => console.log(d))

// Add email recipient
fetch('/api/email-recipients', {
  method: 'POST',
  credentials: 'same-origin',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email: 'test@example.com' })
}).then(r => r.json()).then(d => console.log(d))
```

---

## Performance Optimization

1. **Database**: Run `/api/database/optimize` periodically
2. **Cleanup**: Set retention policy to delete old data
3. **Stream**: MJPEG stream is CPU intensive, use iframe for embedding
4. **Batch Requests**: Group API calls where possible
5. **Caching**: Frontend caches data with auto-refresh intervals

---

## Security Considerations

1. **HTTPS**: Use SSL/TLS in production
2. **SMTP**: Use app-specific passwords, not account passwords
3. **Firewall**: Restrict access to port 5000 on LAN
4. **Backups**: Create and store database backups securely
5. **Logs**: Monitor logs for suspicious activity
6. **Sessions**: Sessions expire on logout or browser close

---

## Troubleshooting API Issues

### 401 Unauthorized
- Check session is valid
- Login again if session expired
- Verify cookies are enabled

### 403 Forbidden
- Check user has admin privileges
- Verify user is authenticated

### 500 Internal Server Error
- Check server logs: `logs/system.log`
- Verify database is accessible
- Check all required fields are provided

### CORS Issues
- Use `credentials: 'same-origin'` in fetch calls
- Ensure requests are to same origin
- Check browser console for CORS errors

---

This technical reference provides complete API documentation and usage examples for developers integrating with or extending the Smart CCTV System.
