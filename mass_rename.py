import os
import tkinter as tk
from tkinter import filedialog, messagebox

def mass_rename(directory, prefix):
    try:
        for filename in os.listdir(directory):
            old_path = os.path.join(directory, filename)

            if os.path.isfile(old_path):
                new_filename = prefix + filename
                new_path = os.path.join(directory, new_filename)

                os.rename(old_path, new_path)
        messagebox.showinfo("Success", f"All files successfully renamed with prefix: {prefix}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

def rename_files():
    directory = folder_path.get()
    prefix = prefix_entry.get()

    if not directory or not prefix:
        messagebox.showwarning("Input required", "Please select a folder and enter a prefix.")
        return

    mass_rename(directory, prefix)

root = tk.Tk()
root.title("Mass File Renamer")

folder_frame = tk.Frame(root)
folder_frame.pack(pady=10)

folder_label = tk.Label(folder_frame, text="Folder:")
folder_label.pack(side=tk.LEFT)

folder_path = tk.StringVar()
folder_entry = tk.Entry(folder_frame, textvariable=folder_path, width=40)
folder_entry.pack(side=tk.LEFT, padx=5)

browse_button = tk.Button(folder_frame, text="Browse", command=browse_folder)
browse_button.pack(side=tk.LEFT)

prefix_frame = tk.Frame(root)
prefix_frame.pack(pady=10)

prefix_label = tk.Label(prefix_frame, text="Prefix:")
prefix_label.pack(side=tk.LEFT)

prefix_entry = tk.Entry(prefix_frame, width=20)
prefix_entry.pack(side=tk.LEFT, padx=5)

rename_button = tk.Button(root, text="Rename Files", command=rename_files)
rename_button.pack(pady=20)

root.mainloop()
