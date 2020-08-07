"""
* Project Name: Crypto
* File Name: test_fileio.py
* Programmer: Kai Prince
* Date: Thu, Aug 06, 2020
* Description: This file contains tests for the FileIO functions.
"""
import pytest
import os
from crypto.fileio import read_file, validate_file, write_file


@pytest.fixture()
def test_files_dir(tmp_path):
    """ Copy mock files to temp directory. """
    FILES_FOLDER = os.path.join(".", "tests", "mock_files")

    # Copy files in test uploads folder to temp directory
    filesToCopy = os.listdir(FILES_FOLDER)
    for f in filesToCopy:
        with open(os.path.join(FILES_FOLDER, f), "rb") as src:
            dest_file = tmp_path / f
            copyfile(src, dest_file)

    yield tmp_path

    # Teardown
    for f in filesToCopy:
        dest_file = tmp_path / f
        print(tmp_path)
        os.remove(dest_file)


def copyfile(source, dest, buffer_size=1024 * 1024):
    """      
    Copy a file from source to dest. source and dest
    must be file-like objects, i.e. any object with a read or
    write method, like for example StringIO.
    """
    while True:
        copy_buffer = source.read(buffer_size)
        if not copy_buffer:
            break
        dest.write_bytes(copy_buffer)


@pytest.mark.parametrize(
    "input,expected", [("read1.txt", "abcdef"), ("read2.txt", "just a test")]
)
def test_read_file(input, expected, test_files_dir):
    # Arrange
    file_name = os.path.join(test_files_dir, input)

    # Act
    result = read_file(file_name)

    # Assert
    assert result == expected


# @pytest.mark.skip("TODO")
@pytest.mark.parametrize(
    "input,expected",
    [("file1.txt", "I went to the market"),
     ("read2.txt", "I went to the market")],
    )
def test_write_file(input, expected, test_files_dir):
    # Arrange
    file_name = os.path.join(test_files_dir, input)
    content = "I went to the market"

    # Act
    # file_buffer = read_file(file_name)
    if write_file(file_name, content):
        result = read_file(file_name)

    # Assert
    assert result == expected

# @pytest.mark.skip("TODO")
@pytest.mark.parametrize(
    "input,expected",
    [("file1.txt", True), ("file", False)],
)
def test_validate_file(input, expected, test_files_dir):
    # Arrange
    file_name = os.path.join(test_files_dir, input)

    # Act
    result = validate_file(file_name)

    # Assert
    assert result == expected

