import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File categories
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
}

def organize_files(folder_path):
    if not folder_path:
        return "No folder selected."

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            moved = False

            for category, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    moved = True
                    break

            if not moved:
                misc_folder = os.path.join(folder_path, "Others")
                os.makedirs(misc_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(misc_folder, filename))

    return "Files organized successfully."

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        status_label.config(text="Organizing...")
        result = organize_files(folder_path)
        status_label.config(text=result)

# GUI
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")

label = tk.Label(root, text="Click the button to choose a folder to organize:")
label.pack(pady=10)

browse_button = tk.Button(root, text="Browse Folder", command=browse_folder)
browse_button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=20)

root.mainloop()
