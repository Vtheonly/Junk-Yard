from greenShell import print_in_green as printG
import os

# Directory containing your files and folders
# directory =r"C:\Users\merse\OneDrive\Documents\Learn\Courses\2 - Engineering\2 - System Design\Systems Design"


directory =r"C:\Users\merse\OneDrive\Documents\Learn\Obsidian Notes\University\GL\1 - Use Case Diagram"

def list_files_in_directory(directory):
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The provided path '{directory}' is not a directory.")
    return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

def list_dirs_in_directory(directory):
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The provided path '{directory}' is not a directory.")
    return [file for file in os.listdir(directory) if os.path.isdir(os.path.join(directory, file))]

def rename_files(old_names, new_names):
    for old_name, new_name in zip(old_names, new_names):
        old_file = os.path.join(directory, old_name)  # Full path of the old file
        new_file = os.path.join(directory, new_name)  # Full path of the new file
        
        if os.path.exists(old_file):
            os.rename(old_file, new_file)
            printG(f"Renamed: {old_file} -> {new_file}")
        else:
            print(f"File not found: {old_file}")

def rename_folders(old_names, new_names):
    for old_name, new_name in zip(old_names, new_names):
        old_dir = os.path.join(directory, old_name)  # Full path of the old directory
        new_dir = os.path.join(directory, new_name)  # Full path of the new directory
        
        if os.path.exists(old_dir):
            os.rename(old_dir, new_dir)
            printG(f"Renamed: {old_dir} -> {new_dir}")
        else:
            print(f"Directory not found: {old_dir}")

# Example usage:
# old_file_names = ['old_file1.mp3', 'old_file2.mp3']
# new_file_names = ['new_file1.mp3', 'new_file2.mp3']
# rename_files(old_file_names, new_file_names)

# old_folder_names = ['old_folder1', 'old_folder2']
# new_folder_names = ['new_folder1', 'new_folder2']
# rename_folders(old_folder_names, new_folder_names)