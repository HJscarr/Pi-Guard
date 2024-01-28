from picamera import PiCamera
from datetime import datetime
import subprocess

# Function to record video for set time with specified frame rate
def record_video(duration, video_file, frame_rate=12):
    
    # Create camera object (OOP) and set resolution and frame-rate using methods
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = frame_rate

    # Record Video
    print("Starting video recording...")

    # Use PiCamera objects methods to record for a specified time
    camera.start_recording(video_file)
    camera.wait_recording(duration)
    camera.stop_recording()
    camera.close()

    print(f"Video recorded at: {video_file}")

    # Return the video file value to the variable
    return video_file

# A function to convert .h264 video to .mp4 video
def convert_to_mp4(video_file):
    # Convert to MP4
    print("Converting to MP4 format...")
    command = f"ffmpeg -framerate {frame_rate} -i {video_file} -c copy {mp4_video_file}"
    subprocess.run(command, shell=True)

    print(f"Video converted and saved as: {mp4_video_file}")

# Record duration
record_duration = 10
frame_rate = 12

# Generate a unique file name with timestamp
timestamp = datetime.now().strftime("%d/%m-%H%M")
video_file = f"/home/js17/video_{timestamp}.h264"
mp4_video_file = f"/home/js17/video_{timestamp}.mp4"

# Call record video function and store return value in h264_video variable
h264_video = record_video(duration, video_file, frame_rate)

# Call convert to mp4 function, no need to save it as a variable as it has no return value
convert_to_mp4(h264_video)