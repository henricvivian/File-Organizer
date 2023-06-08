import os
import shutil

def organize_files(directory, destination_mapping):
    for destination in destination_mapping.values():
        os.makedirs(destination, exist_ok=True)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        for extension, destination in destination_mapping.items():
            if filename.endswith(extension):
                shutil.move(file_path, os.path.join(destination, filename))
                break

    print('Files have been organized!')

def main():
    directory = 'E:'

    destination_mapping = {
        '.doc': 'C:/Users/User/Desktop/Organized/Documents',
        '.docx': 'C:/Users/User/Desktop/Organized/Documents',
        '.pdf': 'C:/Users/User/Desktop/Organized/Documents',
        '.jpg': 'C:/Users/User/Desktop/Organized/Images',
        '.png': 'C:/Users/User/Desktop/Organized/Images',
        '.gif': 'C:/Users/User/Desktop/Organized/Images',
        '.mp3': 'C:/Users/User/Desktop/Organized/Audio',
        '.wav': 'C:/Users/User/Desktop/Organized/Audio',
        '.mp4': 'C:/Users/User/Desktop/Organized/Video',
        '.avi': 'C:/Users/User/Desktop/Organized/Video',
        '.exe': 'C:/Users/User/Desktop/Organized/Executables',
        '.msi': 'C:/Users/User/Desktop/Organized/Executables',
        '.zip': 'C:/Users/User/Desktop/Organized/Archives',
        '.rar': 'C:/Users/User/Desktop/Organized/Archives'
    }

    organize_files(directory, destination_mapping)

if __name__ == "__main__":
    main()
