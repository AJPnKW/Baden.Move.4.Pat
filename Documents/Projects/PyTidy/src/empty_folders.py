# empty_folders.py

import os

def find_empty_folders(directory):
    """Find all empty folders in a directory."""
    empty_folders = []
    for root, dirs, _ in os.walk(directory, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                empty_folders.append(dir_path)
    return empty_folders

def remove_empty_folders(empty_folders):
    """Remove empty folders."""
    for folder in empty_folders:
        os.rmdir(folder)
        print(f"Removed empty folder: {folder}")
