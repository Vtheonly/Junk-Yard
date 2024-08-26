import os
import eyed3  # type: ignore may or may not be avialalbe  pip first
directory_path =  r""

def clear_mp3_metadata(file_path):
    audiofile = eyed3.load(file_path)
    if audiofile is None:
        print(f"Failed to load {file_path}.")
        return
    audiofile.tag.clear()
    audiofile.tag.save()



def clear_metadata_in_directory(directory_path):
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"The provided path '{directory_path}' is not a directory.")
    
    # all mp3 in the directory
    files = [file for file in os.listdir(directory_path) if file.endswith(".mp3")]
    

    for file in files:
        file_path = os.path.join(directory_path, file)
        clear_mp3_metadata(file_path)
        print(f"Cleared metadata for {file}")


clear_metadata_in_directory(directory_path)
