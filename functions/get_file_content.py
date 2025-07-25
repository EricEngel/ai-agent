import os
from os import path
from functions.config import *

def get_file_content(working_directory, file_path):
    current_directory = path.join(working_directory, file_path)
    absolute_path = path.abspath(current_directory)
    # Ensure the resolved absolute path is within the working directory
    if not absolute_path.startswith(path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    # Ensure that it is actually a file
    elif not path.isfile(absolute_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    file_content_string = ""
    with open(absolute_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if len(f.read()) > MAX_CHARS:
            file_content_string += f"[...File {file_path} truncated at {MAX_CHARS} characters]"
    return file_content_string