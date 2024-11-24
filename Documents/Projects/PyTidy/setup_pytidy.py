# Project: PyTidy

# Script to create the project folder strcuture and file place holders

##Resulting Folder Structure:
# After running the script, you’ll get this structure: (or you should)
# PyTidy/
# ├── docs/                  # Documentation
# ├── src/                   # Source code
# │   ├── __init__.py
# │   ├── tidy_files.py      # Main program
# │   ├── duplicate.py       # Duplicate detection
# │   ├── empty_files.py     # Empty file handling
# │   ├── empty_folders.py   # Empty folder handling
# │   ├── big_files.py       # Detect largest files
# │   ├── temporary_files.py # Detect temporary files
# │   ├── similar_images.py  # Find similar images
# │   ├── similar_videos.py  # Find similar videos
# │   ├── same_music.py      # Detect duplicate music files
# │   ├── bad_extensions.py  # Detect mismatched extensions
# │   ├── cache.py           # Cache management
# │   ├── config.py          # Configuration management
# │   ├── utils.py           # Utility functions (logging, helpers)
# ├── tests/                 # Unit tests
# │   ├── test_tidy_files.py
# │   ├── test_duplicate.py
# │   ├── test_empty_files.py
# │   ├── test_empty_folders.py
# │   ├── test_big_files.py
# │   ├── test_temporary_files.py
# │   ├── test_similar_images.py
# │   ├── test_similar_videos.py
# │   ├── test_same_music.py
# │   ├── test_bad_extensions.py
# │   ├── test_cache.py
# ├── data/                  # Sample data
# ├── logs/                  # Logs
# │   ├── placeholder.log
# ├── results/               # Results
# │   ├── placeholder.txt
# ├── cache/                 # Cached data for scans
# │   ├── placeholder.txt
# ├── config/                # Configuration files
# │   ├── default_config.yaml

# -*- coding: utf-8 -*-
import os

def create_pytidy_structure(base_path):
    """
    Create the folder structure and placeholders for the PyTidy project.
    """
    project_structure = {
        "docs": [],
        "src": [
            "__init__.py",
            "tidy_files.py",
            "duplicate.py",
            "empty_files.py",
            "empty_folders.py",
            "big_files.py",
            "temporary_files.py",
            "similar_images.py",
            "similar_videos.py",
            "same_music.py",
            "bad_extensions.py",
            "cache.py",
            "config.py",
            "utils.py",
        ],
        "tests": [
            "test_tidy_files.py",
            "test_duplicate.py",
            "test_empty_files.py",
            "test_empty_folders.py",
            "test_big_files.py",
            "test_temporary_files.py",
            "test_similar_images.py",
            "test_similar_videos.py",
            "test_same_music.py",
            "test_bad_extensions.py",
            "test_cache.py",
        ],
        "data": [],
        "logs": ["placeholder.log"],
        "results": ["placeholder.txt"],
        "cache": ["placeholder.txt"],
        "config": ["default_config.yaml"],
    }

    # Use the base path as the project directory
    project_path = base_path
    os.makedirs(project_path, exist_ok=True)
    print(f"Base project folder created at: {project_path}")

    for folder, files in project_structure.items():
        folder_path = os.path.join(project_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created or verified folder: {folder_path}")

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.exists(file_path):
                print(f"Skipped existing file: {file_path}")
                continue
            try:
                with open(file_path, "w") as f:
                    if file_name.endswith(".py"):
                        f.write(f"# Placeholder for {file_name}\n")
                    elif file_name == "default_config.yaml":
                        f.write("default_threshold: 80\nuse_cache: true\n")
                    else:
                        f.write(f"Placeholder file for {file_name}\n")
                print(f"Created file: {file_path}")
            except Exception as e:
                print(f"Error creating file '{file_name}': {e}")

    print(f"Project structure created successfully at {project_path}")

# Usage
if __name__ == "__main__":
    base_path = r"C:\Users\Lenovo\Documents\Projects\PyTidy"
    create_pytidy_structure(base_path)
