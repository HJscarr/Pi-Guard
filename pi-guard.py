import subprocess
import threading
from picamera import PiCamera
from gpiozero import Buzzer, MotionSensor
from time import sleep, strftime
from datetime import datetime

# Set up the motion sensor and buzzer
pir = MotionSensor(4)
buzzer = Buzzer(16)

# Function to record audio
def record_audio(duration, audio_file_path):
    subprocess.run(["arecord", "-D", "plughw:1,0", "-d", str(duration), "-f", "cd", audio_file_path])

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

# Function to combine audio and video with specified frame rate
def combine_audio_video(audio_file_path, video_file_path, final_output_path, frame_rate=12):
    command = [
        "ffmpeg", "-y",
        "-r", str(frame_rate),
        "-i", video_file_path,
        "-i", audio_file_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-strict", "experimental",
        final_output_path
    ]
    subprocess.run(command, check=True)

def main():
    # Set a recording duration & then wait for motion...
    record_duration = 10
    pir.wait_for_motion()
    print("Motion detected!!! Starting recording...")

    # Sound buzzer for 2 seconds to signal start recording
    buzzer.on()
    sleep(2)
    buzzer.off()

    # Generate unique file names with timestamp
    timestamp = datetime.now().strftime("%d%m-%H%M")
    audio_file = f"/home/pi/audio_{timestamp}.wav"
    video_file = f"/home/pi/video_{timestamp}.h264"
    final_output = f"/home/pi/output_{timestamp}.mp4"

    # Start recording
    audio_thread = threading.Thread(target=record_audio, args=(record_duration, audio_file))
    video_thread = threading.Thread(target=record_video, args=(record_duration, video_file))

    audio_thread.start()
    video_thread.start()

    audio_thread.join()
    video_thread.join()

    # Combine audio and video
    combine_audio_video(audio_file, video_file, final_output, frame_rate=12)
    print(f"Combined video file created at: {final_output}")

# Start the program
main()
