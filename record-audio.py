import subprocess
from datetime import datetime

# Function to record audio
def record_audio(duration, audio_file_path):
    subprocess.run(["arecord", "-D", "plughw:1,0", "-d", str(duration), "-f", "cd", audio_file_path])

# Record duration
record_duration = 10

# Generate a unique file name with timestamp
timestamp = datetime.now().strftime("%d-%m-%H:%M")
audio_file = f"/home/pi/audio_{timestamp}.wav"

# Record Audio
print("Starting audio recording...")
record_audio(record_duration, audio_file)
print(f"Audio recorded at: {audio_file}")
