# Quick Start Guide - Smart CCTV System

## 🚀 Getting Started in 5 Minutes

### Step 1: Start the System
```bash
cd "C:\Users\pavan\Desktop\SMART CCTV"
python main.py
```

The system will initialize and display:
```
2025-11-27 12:36:16,147 - __main__ - INFO - Smart CCTV System initialized
2025-11-27 12:36:16,150 - __main__ - INFO - Smart CCTV System setup complete
```

### Step 2: Open Web Dashboard
Open your browser and navigate to:
```
http://localhost:5000
```

### Step 3: Create Admin Account
You'll be redirected to the **Login** page. Fill in the **"Create Admin"** form:
- **Admin Username**: `admin`
- **Admin Password**: `admin123`
- Click **"Create Admin"** button

### Step 4: Sign In
Now use the created credentials:
- **Username**: `admin`
- **Password**: `admin123`
- Click **"Sign In"**

You'll be redirected to the main **Dashboard**.

---

## 📋 Main Dashboard Features

### Live Preview Section
- **Camera Stream**: Real-time video feed from your camera
- **Start/Stop Buttons**: Control recording manually
- **Status Indicator**: Shows if system is online/offline

### Stats Overview
- **Active Cameras**: Number of configured cameras
- **Recordings**: Total video recordings
- **Recent Events**: Motion detection events
- **Alerts**: Alert notifications triggered

### Motion Analytics
- **Severity Stats**: High/Medium/Low severity motion counts
- **Motion Events**: List of recent motion detections with:
  - Contour count
  - Motion area percentage
  - Severity level
  - Timestamp

---

## ⚙️ Essential Configuration

### 1. Add a Camera
1. Go to **Settings** → **Add Camera**
2. Fill in camera details:
   - **Name**: Give your camera a name (e.g., "Front Door")
   - **Camera Index/Source**: Usually `0` for webcam, or video file path
   - **Width/Height**: Video resolution (default 640x480)
3. Click **"Add Camera"**
4. Camera will start capturing immediately

### 2. Configure Email Alerts
1. Go to **Settings** → **Email Alert Settings**
2. Enter your SMTP configuration:
   - **SMTP Server**: `smtp.gmail.com` (for Gmail)
   - **Port**: `587` (for Gmail with TLS)
   - **Username**: Your email address
   - **Password**: Your app password (or email password)
3. Click **"Save SMTP Config"**

### 3. Add Email Recipients
1. In **Email Alert Settings** section:
   - **Email Address**: Enter recipient email
   - Click **"Add Recipient"**
2. Recipients will appear in the list below
3. Toggle **Enable/Disable** for each recipient
4. Click **Delete** to remove a recipient

---

## 🎬 Recording Video

### Automatic Recording
- Motion is detected automatically
- Videos are recorded when motion happens
- Stored in `recordings/` folder

### Manual Recording
1. Click **"Start"** button on live preview
2. System records video
3. Click **"Stop"** when done

### Manage Recordings
1. Go to **Recordings** tab
2. View all video files
3. **Download**: Save to your computer
4. **Delete**: Remove recording from system

---

## 📸 Managing Snapshots

### Automatic Snapshots
- One snapshot taken when motion is detected
- Stored in `snapshots/` folder
- Includes timestamp in filename

### View Snapshots
1. Go to **Photos** tab
2. Browse all captured images
3. **Download**: Save photo
4. **Delete**: Remove photo

---

## 🚨 Motion Detection & Alerts

### How It Works
1. System continuously monitors camera feed
2. When motion is detected:
   - Motion event is logged with severity
   - Snapshot is taken
   - Recording starts (if enabled)
   - Email alert sent to configured recipients

### Severity Levels
- **Low**: Small motion, minor area
- **Medium**: Moderate motion activity
- **High**: Significant motion, large area

### Alert Status
- Go to **Alerts** tab
- See all triggered alerts
- Check timestamp and alert type

---

## 📊 Monitoring Activity

### Dashboard
- Real-time stats update every 10 seconds
- Live camera preview
- Quick access to all features

### Events Tab
- All motion detection events
- Timestamp and details
- Clear all events option

### Alerts Tab
- Alert notification history
- Alert type and severity
- Clear alerts option

---

## 🛠️ System Settings

### Retention Settings
- **Retention Days**: Delete recordings older than N days
- **Apply Changes**: Cleanup happens automatically

### Motion Sensitivity
- Slider from 1-100
- Higher value = more sensitive detection
- Adjust based on environment

### Database Management
- **Optimize**: Clean up database (VACUUM)
- **Backup**: Create timestamped backup
- **Clear All**: Delete all data (with confirmation)

---

## 🔐 Security

### Your Login
- Keep your admin password secure
- Session expires when you logout or close browser
- Only authenticated users can access system

### Email Configuration
- SMTP password stored in database
- Never shared or transmitted in plain text
- Use app-specific passwords (not account password)

---

## 🐛 Troubleshooting

### System Won't Start
```bash
# Check Python is installed
python --version

# Install dependencies
pip install -r requirements.txt

# Try running again
python main.py
```

### Can't Login
1. Make sure you created an admin account first
2. Check username/password are correct
3. Browser may be blocking cookies - enable them

### Camera Not Showing
1. Check camera is connected
2. Try camera index 0, 1, 2 (different cameras)
3. Check camera isn't used by another application

### Emails Not Sending
1. Verify SMTP server and port are correct
2. Check email/password are correct
3. Try with app-specific password (not account password)
4. Ensure "Less secure app access" is enabled (Gmail)

### Slow Performance
1. Run **Database Optimize** in settings
2. Reduce video resolution if possible
3. Reduce motion detection frequency
4. Clear old recordings and photos

---

## 📞 Common Tasks

### Check System Status
- Live indicator in top-right corner shows "System Online" or "System Offline"
- Green = Online, Red = Offline

### Download a Recording
1. Go to **Recordings**
2. Click filename or **Download** button
3. Video downloads to your computer

### Clear Motion History
1. Go to **Events** tab
2. Click **"Clear All Events"**
3. Confirm when asked

### Reset Everything
1. Go to **Settings** → **Database Management**
2. Click **"Clear All Data"**
3. Confirm deletion
4. System will be reset to fresh state

---

## 📱 Access from Phone

### Local Network
- Get your computer IP: `ipconfig` in PowerShell
- Access from phone: `http://<YOUR_IP>:5000`
- Use same login credentials

### Example
```
Computer IP: 192.168.1.100
Phone access: http://192.168.1.100:5000
```

---

## ✅ Verification Checklist

After setup, verify everything works:
- [ ] Can login with admin account
- [ ] Live camera preview shows
- [ ] Can start/stop recording
- [ ] Motion detector works (move in front of camera)
- [ ] Email alerts configured
- [ ] Snapshots appear in Photos tab
- [ ] Recordings appear in Recordings tab
- [ ] Can view motion statistics

---

## 🎯 Next Steps

1. **Fine-tune Motion Detection**: Adjust sensitivity slider
2. **Configure Email**: Add multiple recipients if needed
3. **Set Retention Policy**: Decide how long to keep data
4. **Test Email Alerts**: Move in front of camera to trigger motion
5. **Download Sample Recording**: Test recording playback
6. **Create Backup**: Save database backup for safety

---

## 💡 Tips & Tricks

1. **Best Camera Placement**: Aim at entry points (doors, windows)
2. **Lighting**: Good lighting improves motion detection
3. **Night Mode**: Consider IR cameras for night recording
4. **Storage**: Monitor disk space for video storage
5. **Backup Schedule**: Create backups regularly
6. **Email Groups**: Add distribution lists as recipients
7. **Multiple Alerts**: Enable multiple recipients for redundancy

---

## 📚 For More Information

See `COMPLETION_SUMMARY.md` for:
- Full feature list
- Complete API endpoints
- Technical architecture
- Database models
- Advanced configuration

---

**Happy Monitoring!** 🎥

If you encounter any issues, check the logs in the `logs/` folder for error details.
