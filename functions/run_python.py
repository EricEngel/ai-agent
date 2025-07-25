import os, subprocess
from os import path

def run_python_file(working_directory, file_path, args=[]):
    current_directory = path.join(working_directory, file_path)
    file_directory = path.dirname(current_directory)
    file_name = path.basename(current_directory)
    absolute_path = path.abspath(current_directory)
    # Ensure the resolved absolute path is within the working directory
    if not absolute_path.startswith(path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not path.exists(absolute_path):
        return f'Error: File "{file_path}" not found.'
    elif not absolute_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    #print(f"Filepath: {absolute_path}")
    result = subprocess.run(["python3", absolute_path] + args, capture_output=True, text=True, cwd=working_directory, timeout=30)
    parts = []
    if result.stdout:
        parts.append(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        parts.append(f"STDERR:\n{result.stderr}")
    output = "\n".join(parts)
    if output == "":
        output = "No output produced."
    return output