import os
from os import path

def get_files_info(working_directory, directory="."):
    current_directory = path.join(working_directory, directory)
    absolute_path = path.abspath(current_directory)
    # Ensure the resolved absolute path is within the working directory
    if not absolute_path.startswith(path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    # Ensure that it is actually a directory
    elif not path.isdir(current_directory):
        return f'Error: "{directory}" is not a directory'

    files = os.listdir(path=absolute_path)
    file_list = ""
    if directory == ".":
        file_list = f"Result for current directory:\n"
    else:
        file_list = f"Result for {directory} directory:\n"
    for file in files:
        full_path = absolute_path + "/" + file
        file_data = f" - {file}: file_size={path.getsize(full_path)} bytes, is_dir={path.isdir(full_path)}"
        file_list += file_data + "\n"
    return file_list