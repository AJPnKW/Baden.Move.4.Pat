# -*- coding: utf-8 -*-
"""
Main entry point for the PyTidy program.
Handles command-line arguments and ensures dependencies are installed.
"""

import subprocess
import sys

# Required dependencies
REQUIRED_PACKAGES = {
    "pytest": "pip install pytest",
    "PyYAML": (
        "pip install PyYAML --no-build-isolation\n"
        "If the above fails:\n"
        "- Upgrade pip, setuptools, and wheel:\n"
        "  pip install --upgrade pip setuptools wheel\n"
        "- On Windows, install Visual C++ Build Tools from:\n"
        "  https://visualstudio.microsoft.com/visual-cpp-build-tools/"
    ),
    "xxhash": "pip install xxhash",
}


def check_dependencies():
    """Check for missing dependencies and provide installation commands."""
    missing_packages = []
    for package, install_command in REQUIRED_PACKAGES.items():
        try:
            __import__(package.lower())
        except ImportError:
            missing_packages.append((package, install_command))

    if missing_packages:
        print("The following required packages are missing:")
        for package, command in missing_packages:
            print(f"- {package}:")
            print(f"  To install, run:\n  {command}\n")
        sys.exit(1)


# Check dependencies before importing other modules
check_dependencies()

# Imports (safe to run after dependency check)
import argparse
from duplicate import find_duplicates, remove_duplicates
from empty_files import find_empty_files, remove_empty_files
from empty_folders import find_empty_folders, remove_empty_folders


def main():
    parser = argparse.ArgumentParser(description="PyTidy - Organize and clean up your files.")
    parser.add_argument("directory", help="Directory to scan and tidy up.")
    parser.add_argument("--remove-duplicates", action="store_true", help="Remove duplicate files.")
    parser.add_argument("--remove-empty-files", action="store_true", help="Remove empty files.")
    parser.add_argument("--remove-empty-folders", action="store_true", help="Remove empty folders.")

    args = parser.parse_args()
    directory = args.directory

    if args.remove_duplicates:
        duplicates = find_duplicates(directory)
        remove_duplicates(duplicates)

    if args.remove_empty_files:
        empty_files = find_empty_files(directory)
        remove_empty_files(empty_files)

    if args.remove_empty_folders:
        empty_folders = find_empty_folders(directory)
        remove_empty_folders(empty_folders)

    print("Tidy-up completed!")


if __name__ == "__main__":
    main()
