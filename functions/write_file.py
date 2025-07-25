import os
from os import path

def write_file(working_directory, file_path, content):
    current_directory = path.join(working_directory, file_path)
    file_directory = path.dirname(current_directory)
    file_name = path.basename(current_directory)
    absolute_path = path.abspath(current_directory)
    # Ensure the resolved absolute path is within the working directory
    if not absolute_path.startswith(path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not path.exists(absolute_path):
        os.makedirs(path.basename(absolute_path))
    
    print(f"Absolute path: {absolute_path}")
    print(f"Directory: {path.basename(absolute_path)}")
    print(f"File: {file_name}")

    with open(absolute_path, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'