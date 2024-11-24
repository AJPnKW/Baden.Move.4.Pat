# empty_files.py

import os

def find_empty_files(directory):
    """Find all empty files in a directory."""
    empty_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) == 0:
                empty_files.append(file_path)
    return empty_files

def remove_empty_files(empty_files):
    """Remove empty files."""
    for file in empty_files:
        os.remove(file)
        print(f"Removed empty file: {file}")
