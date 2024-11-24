# test_duplicate.py

import pytest
from src.duplicate import find_duplicates

def test_find_duplicates(tmpdir):
    file1 = tmpdir.join("file1.txt")
    file2 = tmpdir.join("file2.txt")
    file1.write("Duplicate content")
    file2.write("Duplicate content")
    duplicates = find_duplicates(str(tmpdir))
    assert len(duplicates) == 1
