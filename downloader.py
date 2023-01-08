from pytube import YouTube

# Set the URL of the video you want to download
url = 'https://youtu.be/_YsQ29Bqr6g?list=TLPQMDgwMTIwMjPECwUlCo5YIQ' 

# Create a YouTube object
yt = YouTube(url)

# Set the filename as the video title
filename = yt.title

# Get the first audio stream available
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio stream to the current working directory
audio_stream.download()

from pydub import AudioSegment

# Set the input and output filenames
input_filename = "Lil Baby Type Beat Cinematic.mp4"
output_filename = "Lil Baby Type Beat Cinematic.mp3"


# Load the audio file using pydub
audio = AudioSegment.from_file(input_filename, format="mp4")

# Save the audio file in MP3 format
audio.export(output_filename, format="mp3")