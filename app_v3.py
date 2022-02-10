from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from os import listdir
from os import path
import shutil
from fnmatch import fnmatch

# Define a list of file formats (you can add more formats if needed)
format_list = ["mp4", "mp3", "csv", "xml", "txt", "json", "docx", "ppt", "pptx", "jpg", "jpeg", "png", "gif", "doc", "dat", "sql", "html", "css", "js", "tmp", "dll", "exe", "py", "mov", "iso", "pdf", "zip", "rar", "tar", "msi", "svg"]

root = Tk()

root.geometry("700x330")

app_title = root.title("File Organizer")

bg = Image.open('assets/bg.png')
l = Label(root)
l.place(x=0, y=0, relwidth=1, relheight=1)

# Functions
def on_resize(e):
    image = bg.resize((e.width, e.height), Image.ANTIALIAS)
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)

def sort():
    # Define global variables
    global explorer_entry_source, explorer_entry_destination
    global explorer_button_source, explorer_button_destination
    global sort_source_label_source, sort_source_label_destination

    # Remove left-overs from the organize function
    organize_explorer_entry_source.grid_forget()
    organize_explorer_entry_destination.grid_forget()
    organize_explorer_button_source.grid_forget()
    organize_explorer_button_destination.grid_forget()
    organize_sort_source_label_source.grid_forget()
    organize_sort_source_label_destination.grid_forget()
    completed_label.grid_forget()
    completed_label_2.grid_forget()

    # Select button of current active function
    organize_button.config(borderwidth=1)
    sort_button.config(relief=SUNKEN, borderwidth=5)

    # Define file explorer source
    explorer_entry_source = Entry(root, width=80)
    explorer_entry_source.grid(row=2, column=0, columnspan=1, padx=20, pady=10)

    explorer_button_source = Button(root, text="...", padx=20, pady=3, bg="white", fg="black", activebackground="grey", command=is_pressed_source)
    explorer_button_source.grid(row=2, column=1)

    # Define file explorer destination
    explorer_entry_destination = Entry(root, width=80)
    explorer_entry_destination.grid(row=4, column=0, columnspan=1, padx=20, pady=10)

    explorer_button_destination = Button(root, text="...", padx=20, pady=3, bg="white", fg="black", activebackground="grey", command=is_pressed_destination)
    explorer_button_destination.grid(row=4, column=1)

    # Define Labels
    sort_source_label_source = Label(root, text="Sort: Select your source folder", font=1, fg="black", bg="white")
    sort_source_label_source.grid(row=1, column=0, padx=20, sticky=S + W)

    sort_source_label_destination = Label(root, text="Sort: Select your destination folder", font=1, fg="black", bg="white")
    sort_source_label_destination.grid(row=3, column=0, padx=20, sticky=S + W)

    # Define execute button
    execute_button = Button(root, text="Launch", padx=20, pady=3, bg="white", fg="black", activebackground="grey", command=sort_execution)
    execute_button.grid(row=5, column=0, columnspan=1, pady=10)

def sort_execution():
    global completed_label
    source_input = sp
    destination_input = dp
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
    completed_label = Label(root, text="Completed!", font=1, bg="green", fg="black", padx=20, pady=3)
    completed_label.grid(row=5, column=1, pady=20, sticky=W)

def organize():
    # Define global variables
    global organize_explorer_entry_source, organize_explorer_entry_destination
    global organize_explorer_button_source, organize_explorer_button_destination
    global organize_sort_source_label_source, organize_sort_source_label_destination

    # Remove left-overs from the sort function
    explorer_entry_source.grid_forget()
    explorer_entry_destination.grid_forget()
    explorer_button_source.grid_forget()
    explorer_button_destination.grid_forget()
    sort_source_label_source.grid_forget()
    sort_source_label_destination.grid_forget()
    completed_label.grid_forget()
    completed_label_2.grid_forget()

    # Select button of current active function
    sort_button.config(borderwidth=1)
    organize_button.config(relief=SUNKEN, borderwidth=5)

    # Define file explorer source
    organize_explorer_entry_source = Entry(root, width=80)
    organize_explorer_entry_source.grid(row=2, column=0, columnspan=1, padx=20, pady=10)

    organize_explorer_button_source = Button(root, text="...", padx=20, pady=3, bg="white", fg="black", activebackground="grey", command=is_pressed_source)
    organize_explorer_button_source.grid(row=2, column=1)

    # Define file explorer destination
    organize_explorer_entry_destination = Entry(root, width=80)
    organize_explorer_entry_destination.grid(row=4, column=0, columnspan=1, padx=20, pady=10)

    organize_explorer_button_destination = Button(root, text="...", padx=20, pady=3, bg="white", fg="black", activebackground="grey", command=is_pressed_destination)
    organize_explorer_button_destination.grid(row=4, column=1)

    # Define Labels
    organize_sort_source_label_source = Label(root, text="Organize: Select your source folder", font=1, fg="black", bg="white")
    organize_sort_source_label_source.grid(row=1, column=0, padx=20, sticky=S + W)

    organize_sort_source_label_destination = Label(root, text="Organize: Select your destination folder", font=1, fg="black", bg="white")
    organize_sort_source_label_destination.grid(row=3, column=0, padx=20, sticky=S + W)

    # Define execute button
    execute_button = Button(root, text="Launch", padx=20, pady=3, bg="white", fg="black", activebackground="grey", command=organize_execution)
    execute_button.grid(row=5, column=0, columnspan=1, pady=10)

def organize_execution():
    global completed_label_2
    source = sp
    destination = dp
    for file in listdir(f"{source}/"):
        filename = path.basename(file)
        match = fnmatch(filename, f"*{filename[0:5]}*")
        naming = filename[0:11]  # 0:11 defines how long the name of the folder will be, the bigger the number, the more complete the name will be.
        # Create a folder for each file with the same name
        if match and not path.isdir(destination + "/" + naming):
            print(f"Creating new folder {naming}...")
            os.mkdir(destination + "/" + naming)
    print(f"Folders created! You can find them in {destination}.")
    for file in listdir(f"{source}/"):
        filename = path.basename(file)
        match = fnmatch(filename, f"*{filename[0:5]}*")
        naming2 = filename[0:11]
        # Move files with the same name into the right folder
        if match:
            print(f"Moving files to {naming2}...")
            try:
                shutil.move(source + "/" + file, destination + "/" + naming2)
            except shutil.Error:
                print("Can not move files into them self.")
    print(f"All files moved! You can find them in the {destination} path.")
    completed_label_2 = Label(root, text="Completed!", font=1, bg="green", fg="black", padx=20, pady=3)
    completed_label_2.grid(row=5, column=1, pady=20, sticky=W)

def browse_files_source():
    folder_path = filedialog.askdirectory(initialdir="/", title="Select a Folder")
    explorer_entry_source.insert(0, folder_path)
    organize_explorer_entry_source.insert(0, folder_path)
    explorer_entry_source.config(state=DISABLED)
    organize_explorer_entry_source.config(state=DISABLED)
    return folder_path

def browse_files_destination():
    folder_path = filedialog.askdirectory(initialdir="/", title="Select a Folder")
    explorer_entry_destination.insert(0, folder_path)
    organize_explorer_entry_destination.insert(0, folder_path)
    explorer_entry_destination.config(state=DISABLED)
    organize_explorer_entry_destination.config(state=DISABLED)
    return folder_path

def is_pressed_source():
    global sp
    sp = browse_files_source()

def is_pressed_destination():
    global dp
    dp = browse_files_destination()

# Define empty file explorer
organize_explorer_entry_source = Entry()
organize_explorer_button_source = Button()
explorer_entry_source = Entry()
explorer_button_source = Button()
organize_explorer_entry_destination = Entry()
organize_explorer_button_destination = Button()
explorer_entry_destination = Entry()
explorer_button_destination = Button()
organize_sort_source_label_source = Label()
organize_sort_source_label_destination = Label()
sort_source_label_source = Label()
sort_source_label_destination = Label()
completed_label = Label()
completed_label_2 = Label()

# Define Frames
buttons_frame = Frame(root, padx=10, pady=10, bg="black", relief=SUNKEN, highlightbackground="yellow", highlightcolor="yellow", highlightthickness=1, bd=0)
buttons_frame.grid(row=0, column=0, padx=50, pady=30)

buttons_frame2 = Frame(buttons_frame, padx=10, pady=10, bg="black")
buttons_frame2.grid(row=0, column=1)

# Define Buttons
sort_button = Button(buttons_frame, text="Sort", font=20, padx=20, pady=5, bg="white", fg="black", activebackground="grey", command=sort)
sort_button.grid(row=0, column=0, padx=20)

organize_button = Button(buttons_frame2, text="Organize", font=20, padx=20, pady=5, bg="white", fg="black", activebackground="grey", command=organize)
organize_button.grid(row=0, column=0, padx=20)

# Background auto re-size
l.bind('<Configure>', on_resize)

root.mainloop()
