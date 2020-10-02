# This library  allows the user to execute shell commands with a python script.
import os
# This library  allows the user to find file path.
from pathlib import Path 

# User inputs the name of a file inside the target folder.
project_file_name = input("Please enter file name: ")

# User inputs the the path of the file that they wrote for the first input.
project_file_directory = input("Please enter the directory: ") 

"""
This function looks for and finds the desired file. You can specify a parent directory for the function to look for, however if you have no idea where a file is; this function will find it for you, just slower. If you have no idea where a file is, just type "/".
"""
def find_the_project(file_name, directory_name):
    files_found = [ ]
    for path, subdirs, files in os.walk(directory_name):
        for name in files:
            if(file_name == name):
                file_path = os.path.join(path, name)
                files_found.append(file_path)
# Returns the path.
    return files_found[0] 

# Inıtializes the path of the file.
project_file_path = Path(find_the_project(project_file_name, project_file_directory))

# Initializes the string that will be executed in the shell.
get_shell_statement = "flake8 " + str(project_file_path)
# Executes the predefined string in the shell.
os.system(get_shell_statement)