####Required Software to run this script#####
# (1) Install Python for Windows.
# (2) Install moviepy (run "pip install moviepy" via CMD (admin mode))
# (3) Install ImageMagick: Make sure ImageMagick is installed on your system. 
#     You can download it from ImageMagick’s official website.
#     Set the ImageMagick Path: Ensure that the path to the ImageMagick binary is correctly set in your environment variables or within your script (see below).

# Run this script in CMD by "python <yourScriptFileName.py>"

# This script create as many videos (count in this script) as required, each video is unique.
# You can also set the duration of the videos, here.

from moviepy.editor import TextClip, CompositeVideoClip
from moviepy.config import change_settings
from datetime import datetime
import random
import os
import zipfile
import concurrent.futures

# Set the path to ImageMagick
change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

# Get the current time
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Print the current time
print("Video Generator Started at:", start_time)

def generate_video(text, color, duration, filename, resolution=(640, 480), fps=24):
    # Create a text clip
    text_clip = TextClip(text, fontsize=50, color='white', bg_color=color, size=resolution)
    text_clip = text_clip.set_duration(duration)

    # Create a composite video clip
    video = CompositeVideoClip([text_clip], size=resolution)
    
    # Write the video to a file with H.264 encoding
    video.write_videofile(filename, codec='libx264', fps=fps, threads=4)  # Use 4 threads for faster encoding

# List of texts and colors for different videos
texts = ["Hello World!", "Python is awesome!", "Py is cool!", "Short video", "Video number",
         "Hello Earth!!!", "Python is good!", "Py is great!", "Short vid", "Video magic",
         "Hello Mars!", "Python is fantastic!", "Py is hot!", "Short long video", "Video Play"]
colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"]


# Directory to store the video files
output_dir = "videos"
os.makedirs(output_dir, exist_ok=True)


# Function to generate a single video with random text and color
def generate_random_video(i):    
    color = random.choice(colors)
    filename = os.path.join(output_dir, f"video_{i+1}.mp4")
    text = f"Video File: video_{i+1}.mp4\n {random.choice(texts)}"
    generate_video(text, color, video_duration, filename, resolution=(640, 480), fps=24)
    print(f'{filename} created successfully.')

# Generate multiple videos in parallel
video_count = 1  # Change this to the number of videos you want to create
video_duration = 1.1  # This is video duration in seconds, ensure it is at least 1.1 (C&E has issues uploading 1second or less)

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(generate_random_video, i) for i in range(video_count)]
    for future in concurrent.futures.as_completed(futures):
        future.result()
        
# Get the current time
finished_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Zip the video files
zip_filename = "videos.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, _, files in os.walk(output_dir):
        for file in files:
            zipf.write(os.path.join(root, file), arcname=file)

print(f"{video_count} video files have been generated and zipped into {zip_filename}.")
print("All videos created successfully at:", finished_time)