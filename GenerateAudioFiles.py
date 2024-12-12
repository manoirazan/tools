#You may need to install the following by using your favourite command line tool (powershell will do)
#Install scipy: "pip install scipy" 
#Install pydub: "pip install numpy pydub"
#Install ffmpeg: "choco install ffmpeg"

import numpy as np
from scipy.io.wavfile import write
import os

def generate_random_audio(filename, duration=2, sample_rate=44100):
    # Generate random audio data
    audio_data = np.random.uniform(-1, 1, duration * sample_rate)
    audio_data = np.int16(audio_data * 32767)  # Convert to 16-bit PCM format

    # Write the audio data to a WAV file
    write(filename, sample_rate, audio_data)

def convert_wav_to_mp3(wav_filename, mp3_filename):
    from pydub import AudioSegment
    # Convert WAV to MP3
    audio = AudioSegment.from_wav(wav_filename)
    audio.export(mp3_filename, format="mp3")

def create_random_audio_files(num_files):
    # Create a folder named "AudioFiles" if it doesn't exist
    if not os.path.exists("AudioFiles"):
        os.makedirs("AudioFiles")
    for i in range(num_files):
        wav_filename = f"random_audio_{i+1}.wav"
        mp3_filename = f"AudioFiles/random_audio_{i+1}.mp3"
        
        # Generate random WAV file
        generate_random_audio(wav_filename)
        
        # Convert WAV file to MP3
        convert_wav_to_mp3(wav_filename, mp3_filename)
        
        # Remove the intermediate WAV file
        os.remove(wav_filename)

# Specify the number of random audio files to create
num_files = 5

# Create the random audio files
create_random_audio_files(num_files)

print(f"{num_files} random audio MP3 files have been created in the 'AudioFiles' folder.")