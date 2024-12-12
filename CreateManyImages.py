####Required Software to run this script#####
# (1) Install Python for Windows.
# (2) Install moviepy (run "pip install pillow" via CMD (admin mode))

# Run this script in CMD by "python <yourScriptFileName.py>"

# This script create as many image files (count in this script) as required, each image is unique.
# It also zips up the images. 

import os
from PIL import Image, ImageDraw, ImageFont
import random
import zipfile
import time

def create_images(directory, num_images):
    os.makedirs(directory, exist_ok=True)
    start_time = time.time()
    for i in range(num_images):
        img = Image.new('RGB', (250, 250), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        
        # Add text to the image
        draw = ImageDraw.Draw(img)
        text = f"Image File:\nimage_{i+1}.png"
        font = ImageFont.truetype("arial.ttf", 23)  # Change 20 to your desired font size
        textbbox = draw.textbbox((0, 0), text, font=font)
        textwidth, textheight = textbbox[2] - textbbox[0], textbbox[3] - textbbox[1]        
        width, height = img.size
        x = (width - textwidth) / 2
        y = (height - textheight) / 2
        draw.text((x, y), text, font=font, fill=(255, 255, 255))        
        
        # Save image
        img.save(f'{directory}/image_{i+1}.png')        
        
        # Show progress status every 100 images
        if (i + 1) % 100 == 0:
            elapsed_time = time.time() - start_time
            print(f"{i + 1} images created. Elapsed time: {elapsed_time:.2f} seconds.")
    
    print(f"{num_images} images have been generated and saved in the '{directory}' directory.")

def zip_images(directory, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                zipf.write(file_path, arcname=file)
    print(f"The images have been zipped into '{zip_name}'.")

# Number of images to create
numberOfImages = 4000

# Generate and zip images
create_images('images', numberOfImages)
zip_images('images', 'images.zip')