# duplicate.py

import os
import hashlib

def hash_file(file_path):
    """Generate MD5 hash for a file."""
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(directory):
    """Find duplicate files in a directory."""
    file_hash_map = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)

            if file_hash in file_hash_map:
                duplicates.append((file_path, file_hash_map[file_hash]))
            else:
                file_hash_map[file_hash] = file_path

    return duplicates

def remove_duplicates(duplicates):
    """Remove duplicate files."""
    for duplicate, _ in duplicates:
        os.remove(duplicate)
        print(f"Removed duplicate: {duplicate}")
