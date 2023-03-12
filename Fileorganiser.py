import os
import shutil

# Set the directory to be organized
directory = 'E:'

# Set the destination directory for each file type
document_dest = 'C:/Users/User/Desktop/Organized/Documents'
image_dest = 'C:/Users/User/Desktop/Organized/Images'
audio_dest = 'C:/Users/User/Desktop/Organized/Audio'
video_dest = 'C:/Users/User/Desktop/Organized/Video'
executable_dest = 'C:/Users/User/Desktop/Organized/Executables'
archive_dest = 'C:/Users/User/Desktop/Organized/Archives'
other_dest = 'C:/Users/User/Desktop/Organized/Others'

# Create the destination directories if they don't exist
os.makedirs(document_dest, exist_ok=True)
os.makedirs(image_dest, exist_ok=True)
os.makedirs(audio_dest, exist_ok=True)
os.makedirs(video_dest, exist_ok=True)
os.makedirs(executable_dest, exist_ok=True)
os.makedirs(archive_dest, exist_ok=True)
os.makedirs(other_dest, exist_ok=True)

# Loop through each file in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    # Determine the file type using the file extension
    if filename.endswith('.doc') or filename.endswith('.docx') or filename.endswith('.pdf'):
        destination = document_dest
    elif filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.gif'):
        destination = image_dest
    elif filename.endswith('.mp3') or filename.endswith('.wav'):
        destination = audio_dest
    elif filename.endswith('.mp4') or filename.endswith('.avi'):
        destination = video_dest
    elif filename.endswith('.exe') or filename.endswith('.msi'):
        destination = executable_dest
    elif filename.endswith('.zip') or filename.endswith('.rar'):
        destination = archive_dest
    else:
        destination = other_dest

    # Move the file to its destination directory
    shutil.move(file_path, os.path.join(destination, filename))

print('Files have been organized!')
