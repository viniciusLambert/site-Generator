import os
import shutil


def copy_directory(source_directory: str, destination_directory: str):

    if not os.path.exists(destination_directory):
        raise Exception(f"destination directory {destination_directory} don't exist")
    
    if not os.path.exists(source_directory):
        raise Exception(f"source directory {source_directory} don't exist")
    
    os.makedirs(destination_directory)
    files_to_migrate = os.listdir(source_directory)
    for file in files_to_migrate:
        source_file_path = os.path.join(source_directory, file)
        destination_file_path = os.path.join(destination_directory, file)
        if(os.path.isfile(source_file_path)):
            shutil.copy(source_file_path, destination_file_path)
        else:
            os.makedirs(destination_file_path)
            copy_directory(source_file_path, destination_file_path)
