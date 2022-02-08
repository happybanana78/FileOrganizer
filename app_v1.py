import os
from os import listdir
from os import path
import shutil
from fnmatch import fnmatch
import time

files_path = "files/"

format_list = ["mp4", "mp3", "csv", "xml", "txt", "json"]

print("Alursers File Organizer")
options = '''
Use "fadd" command to add a supported file format
Use "organize" to start the organizer program
Use "sort" to sort through files with a specific format
Use "help" to see this list again
Use "quit" to exit the program
'''
print(options)

def format_add():
    while True:
        format_input = input("Write the format you wanna add (example: mp4, docx, ecc.) or use 'back' command to go back: ")
        if "." in format_input:
            print("Write your format without any dot(.)!")
        elif format_input == "back":
            break
        else:
            print("Added! (Remember to add it again if you restart the program)")
            break


def main_loop():
    for item in format_list:
        while True:
            type_input = input(
                "Enter the file format are you looking for (example: mp3, mp4, csv, ecc..), or use 'back' to go back to the main section: ")
            if type_input == item:
                dir_input = input("How would you like to name the output folder? \n")
                folder_name = dir_input
                open_folder = path.join(folder_name)
                os.mkdir(open_folder)
                print(f"Folder {folder_name} created in current directory.\n")
                user_input = input("Enter file name Keyword: ")
                for file in listdir(files_path):
                    filename = path.basename(file)
                    keyword = fnmatch(filename, f"*{user_input}*")
                    file_type = fnmatch(filename, f"*.{type_input}")
                    if keyword and file_type:
                        print(filename)
                        print("Coping...")
                        time.sleep(1)
                        shutil.move(files_path + file, folder_name)
                        print("Copy completed!")
                        print("Reloading the organizer module...")
                        time.sleep(1)
                    else:
                        print("No file found with specified keyword.")
            elif type_input == "fadd":
                format_add()
            elif type_input == "list":
                print("Default supported formats:")
                print(format_list)
            elif type_input == "back":
                return
            else:
                print("Unsupported Format, use the 'list' command to see the supported formats,")
                print("or use the 'fadd' command to add the desired format.")
            break


def sorting():
    while True:
        fin = False
        extension_input = input("What file format (extension) are you looking for? ")
        for item in format_list:
            if extension_input == "fadd":
                format_add()
                break
            elif extension_input == "list":
                print("Default supported formats:")
                print(format_list)
                break
            elif extension_input == item:
                path_input = input("Enter the complete path to the directory (folder) you wanna check (don't forget the / at the end): \n")
                folder_create_input = input("Enter the name for the folder you wanna create to sort the files into: \n")
                folder_name = folder_create_input
                open_folder = path.join(folder_name)
                os.mkdir(open_folder)
                print(f"New {folder_name} folder created.\n")
                for file in listdir(path_input):
                    try:
                        if fnmatch(file, f"*.{extension_input}"):
                            print(file)
                            shutil.move(path_input + file, folder_name + "/" + file)
                            print("Moving...")
                            fin = True
                    except FileNotFoundError:
                        print("The path to your directory was typed wrong or doesn't exist.\n")
                        break
                print(f"File move Completed! You can now find your sorted files in the {folder_create_input} folder.")
            elif extension_input == "back":
                return
            else:
                if fin:
                    return
                print("Unsupported Format, use the 'list' command to see the supported formats,")
                print("or use the 'fadd' command to add the desired format.")
                print("Use 'back' to go back.")
                break


def help_command():
    print(options)


def quit_command():
    print("Goodbye!")


while True:
    init_input = input("> ").lower()
    if init_input == "fadd":
        format_add()
    elif init_input == "help":
        help_command()
    elif init_input == "quit":
        quit_command()
        break
    elif init_input == "organize":
        main_loop()
    elif init_input == "sort":
        sorting()
    else:
        print("Command not found! Use 'help' command for the command list.")
