import os ## The library import that allows the user to execute shell commands with a python script.
from pathlib import Path ## The library import that allows the user to find file path.


project_file_name = input("Please enter the name of a file in the project folder that you want to create 'requirements.txt' for:    ") ## User inputs the name of a file inside the target folder.
project_file_directory = input("Please enter the directory that may contain the folder:    ") ## User inputs the the path of the file that they wrote for the first input.


## This function looks for and finds the desired file. You can specify a parent directory for the fundtion to look for, however if you have no idea where a file is; this functio will find it for you, just slower. If you have no idea where a file is, just type "/".
def find_the_project(file_name, directory_name):
    files_found = []
    for path, subdirs, files in os.walk(directory_name):
        for name in files:
            if(file_name == name):
                file_path = os.path.join(path, name)
                files_found.append(file_path)

    return files_found[0] ## Return the path.


project_file_path = Path(find_the_project(project_file_name, project_file_directory)) ## Inıtialize the path of the file.
project_folder = project_file_path.parent ## Initialize the parent directory of the file path.


get_req_statement = "pipreqs " + str(project_folder) ## Initialize the string that will be executed in the shell.
os.system(get_req_statement)  ## Execute the predefined string in the shell.
