import os
from os import listdir
from os import path
import shutil
from fnmatch import fnmatch
import time

print("Alursers File Organizer")
options = '''
Use "organize" to start the organizer program
Use "sort" to sort through files with a specific format
Use "auto" to sort all files in different folders depending on their extension.
Use "help" to see this list again
Use "quit" to exit the program
'''
print(options)

# Define a list of file formats (you can add more formats if needed)
format_list = ["mp4", "mp3", "csv", "xml", "txt", "json", "docx", "ppt", "pptx", "jpg", "jpeg", "png", "gif", "doc", "dat", "sql", "html", "css", "js", "tmp", "dll", "exe", "py", "mov", "iso", "pdf", "zip", "rar", "tar", "msi", "svg"]

def organize():
    while True:
        # Get user input to the source folder
        source = input("Enter the path to the source folder: ")
        if path.isdir(source):
            break
        else:
            print("Path not found!")
    while True:
        # Get user input for destination folder
        destination = input("Enter the path where all the new folders and files will be stored: ")
        if path.isdir(destination):
            break
        else:
            print("Path not found!")
    for file in listdir(f"{source}/"):
        filename = path.basename(file)
        match = fnmatch(filename, f"*{filename[0:5]}*")
        naming = filename[0:11]  # 0:11 defines how long the name of the folder will be, the bigger the number, the more complete the name will be.
        # Create a folder for each file with the same name
        if match and not path.isdir(destination + "/" + naming):
            print(f"Creating new folder {naming}...")
            os.mkdir(destination + "/" + naming)
    print(f"Folders created! You can find them in {destination}.")
    time.sleep(1)
    for file in listdir(f"{source}/"):
        filename = path.basename(file)
        match = fnmatch(filename, f"*{filename[0:5]}*")
        naming2 = filename[0:11]
        # Move files with the same name into the right folder
        if match:
            print(f"Moving files to {naming2}...")
            shutil.move(source + "/" + file, destination + "/" + naming2)
    print(f"All files moved! You can find them in the {destination} path.")


def format_choice():
    while True:
        # Get user input for file format
        extension_input = input("What file format (extension) are you looking for? ").lower()
        for item in format_list:
            if "." in extension_input:
                print("Type the format type without any dot(.)")
                break
            elif extension_input == item:
                user_ext = extension_input
                return sort_path_choice(user_ext)


def sort_path_choice(ext):
    while True:
        # Get user input for source folder
        source_input = input("Enter the complete path to the directory (folder) you wanna check: \n")
        if path.isdir(source_input):
            break
        else:
            print("Path Not found!")
    while True:
        # Get user input for destination folder
        destination_input = input("Enter complete path to the folder you wanna save your files in:  \n")
        for file in listdir(source_input):
            try:
                # Move files to the destination folder
                if fnmatch(file, f"*.{ext}"):
                    print(file)
                    shutil.move(source_input + "/" + file, destination_input + "/" + file)
                    print("Moving...")
            except FileNotFoundError:
                print("The path to your directory was typed wrong or doesn't exist.\n")
                break
        print(f"File move Completed! You can now find your sorted files at {destination_input}.")
        break


def auto_sort():
    while True:
        # Get user input for source path
        source_input = input("Enter the complete path to the directory (folder) you wanna check: \n")
        if path.isdir(source_input):
            break
        else:
            print("Path Not found!")
    while True:
        # Get user input for destination path
        destination_input = input("Enter complete path to the folder you wanna save your files in:  \n")
        for file in listdir(source_input):
            filename = path.basename(file)
            try:
                for ext in format_list:
                    # Create a folder for each file type
                    if not path.isdir(destination_input + "/" + ext):
                        os.mkdir(destination_input + "/" + ext)
                        # Move files to the correct folder
                    if fnmatch(filename, f"*.{ext}"):
                        print(file)
                        try:
                            shutil.move(source_input + "/" + file, destination_input + "/" + ext)
                        except shutil.Error:
                            print("Found files that already exist! This files will remain in the initial folder.")
                        print("Moving...")
            except FileNotFoundError:
                print("The path to your directory was typed wrong or doesn't exist.\n")
                break
                # Remove empty folders
        for folder in listdir(destination_input):
            if len(listdir(destination_input + "/" + folder)) == 0:
                os.rmdir(destination_input + "/" + folder)
        print(f"File move Completed! You can now find your sorted files at {destination_input}.")
        break


def help_command():
    print(options)


def quit_command():
    print("Goodbye!")


# Main Loop
while True:
    init_input = input("> ").lower()
    if init_input == "help" or init_input == "h":
        help_command()
    elif init_input == "quit" or init_input == "q":
        quit_command()
        break
    elif init_input == "organize":
        organize()
    elif init_input == "sort":
        format_choice()
    elif init_input == "auto":
        auto_sort()
    else:
        print("Command not found! Use 'help' command for the command list.")
