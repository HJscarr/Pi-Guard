from picamera import PiCamera
from datetime import datetime

# Function to record video with reduced resolution and frame rate
def record_video(duration, video_file, frame_rate):
    
    # Create camera object (OOP) and set resolution and frame-rate using methods
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = frame_rate
    
    # Record Video
    print("Starting video recording...")

    # Use PiCamera object methods to record for a specific time
    camera.start_recording(video_file)
    camera.wait_recording(duration)
    camera.stop_recording()
    camera.close()

    print(f"Video file recorded at {video_file}")

# Record duration
record_duration = 10

# Generate a unique file name with timestamp
timestamp = datetime.now().strftime("%d/%m-%H%M")
video_file = f"/home/pi/video_{timestamp}.h264"

# Record Video
print("Starting video recording...")
record_video(record_duration, video_file)
print(f"Video recorded at: {video_file}")