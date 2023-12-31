from picamera import PiCamera
from datetime import datetime

# Record duration
duration   = 10
frame_rate = 12

# Generate a unique file name with timestamp
timestamp = datetime.now().strftime("%d-%m-%H:%M")
video_file = f"/home/pi/video_{timestamp}.h264"

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = frame_rate

# Record Video
print("Starting video recording...")

camera.start_recording(video_file)
camera.wait_recording(duration)
camera.stop_recording()
camera.close()

print(f"Video recorded at: {video_file}")
