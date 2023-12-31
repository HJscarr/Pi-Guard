from picamera import PiCamera
from datetime import datetime
import subprocess

# Record duration
duration   = 10
frame_rate = 12

# Generate a unique file name with timestamp
timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
h264_video_file = f"/home/js17/video_{timestamp}.h264"
mp4_video_file = f"/home/js17/video_{timestamp}.mp4"

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = frame_rate

# Record Video
print("Starting video recording...")

camera.start_recording(h264_video_file)
camera.wait_recording(duration)
camera.stop_recording()
camera.close()

print(f"Video recorded at: {h264_video_file}")

# Convert to MP4
print("Converting to MP4 format...")
command = f"ffmpeg -framerate {frame_rate} -i {h264_video_file} -c copy {mp4_video_file}"
subprocess.run(command, shell=True)

print(f"Video converted and saved as: {mp4_video_file}")
