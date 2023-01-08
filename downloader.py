from pytube import YouTube
from pytube import Playlist
from pydub import AudioSegment

get_Playlist_URL = input("Please paste the YouTube URL here: ")

# Create the playlist object
playlist = Playlist(get_Playlist_URL)
print("Processing...")

# Iterate over the playlist object and download each video
for video in playlist:
    # Set the URL of the video you want to download
    url = video

    # Create a YouTube object
    yt = YouTube(url)

    # Set the filename as the video title
    filename = yt.title
    filename = filename.replace('.', '')
    if "\"" in filename:
        filename = filename.replace('\"', '')
    if "$" in filename:
        filename = filename.replace('$', '')
    print(filename)
     
    # Get the first audio stream available
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio stream to the current working directory
    audio_stream.download("./Streams/")
    print(f"The Mp4 audio stream of {filename} has been downloaded")

    # Set the input and output filenames
    input_filename = f"{filename}.mp4"
    output_filename = f"{filename}.mp3"


    # Load the audio file using pydub
    audio = AudioSegment.from_file(f"./Streams/{input_filename}", format="mp4")

    # Save the audio file in MP3 format
    audio.export(f"./MP3 Files/{output_filename}", format="mp3")
    print(f"The MP3 Audio file of {filename} is now available")
    print()
    print("Downloading the next file:")