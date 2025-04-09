import os # To Handle file, paths, etc.
import shutil # To Move files.
from pathlib import Path # To Handle paths

# If you want to organize other files in my case i just want to organize download folder
# source_folder = ""

# Getting the directory of download folder
source_folder = str(Path.home() / "Downloads")
print(source_folder)

# Define categories
files_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".ico", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".wma"],
    "Video": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php", ".rb", ".go"],
    "Executables": [".exe", ".msi", ".app", ".dmg"],
    "Others": []
}

# Creating folders for each category
for folder in files_categories:
    # Creating folders 
    #? Step 01 (one line)
    # os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

    #? Step 02 (multiple lines)
    new_folder = os.path.join(source_folder, folder)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

# Going through each file in the folder
for file_name in os.listdir(source_folder):
    # getting file path
    file_path = os.path.join(source_folder, file_name)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # File Extensions
    file_ext = os.path.splitext(file_name)[1].lower()

    # Flag for tracking files
    moved = False

    for folder, extensions in files_categories.items():
        if file_ext in extensions:
            # Moving file to the corresponding folder
            shutil.move(file_path, os.path.join(source_folder, folder, file_name))
            print(f"Moved {file_name} to {folder}")
            moved = True
            break
    
    if not moved:
        shutil.move(file_path, os.path.join(source_folder, "Others", file_name))
        print(f"Moved {file_name} to Others")

print("\n🎉 All files have been organized!")