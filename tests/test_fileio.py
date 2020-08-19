"""
* Project Name: Crypto
* File Name: test_fileio.py
* Programmer: Kai Prince
* Date: Thu, Aug 06, 2020
* Description: This file contains tests for the FileIO functions.
"""
import pytest
import os
from crypto.fileio import read_file, validate_file, write_file, check_write, convert_ext, open_file
from crypto.strategy import SeanStrategy


@pytest.fixture()
def test_files_dir(tmp_path):
    """ Copy mock files to temp directory. """
    FILES_FOLDER = os.path.join(".", "tests", "mock_files")

    # Copy files in test uploads folder to temp directory
    files_to_copy = os.listdir(FILES_FOLDER)
    for f in files_to_copy:
        with open(os.path.join(FILES_FOLDER, f), "rb") as src:
            dest_file = tmp_path / f
            copyfile(src, dest_file)

    yield tmp_path

    # Teardown


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
    [("write1.txt", "abcdef"),
     ("write2.txt", "I went to the market")],
)
def test_write_file(input, expected, test_files_dir):
    # Arrange
    file_name = os.path.join(test_files_dir, input)

    # Act
    write_file(file_name, expected)

    # Assert
    result = read_file(file_name)
    assert result == expected


# @pytest.mark.skip("TODO")
@pytest.mark.parametrize(
    "input,expected",
    [("write1.txt", False), ("read1.txt", True)],
)
def test_validate_file(input, expected, test_files_dir):
    # Arrange
    file_name = os.path.join(test_files_dir, input)

    # Act
    result = validate_file(file_name)

    # Assert
    assert result == expected


#
# FUNCTION      :   test_valide_write()
# DESCRIPTION   :   This function ensures the content in a file is properly written.
#                   It writes to a file, should open the written file and check
#                   if the file_buffer that was written to the file is exactly the same in the opened file.
# PARAMETERS    :
# RETURNS       :

@pytest.mark.parametrize(
    "file_name, file_buffer, expected",
    [("read1.txt", "abcdef", True), ("read2.txt", "zyxwuv", False)],
)
def test_validate_write(file_name, file_buffer, expected, test_files_dir):
    # Arrange
    file_name = os.path.join(test_files_dir, file_name)
    # Act
    try:
        check_write(file_buffer, file_name)
        assert True
    except IOError:
        assert False
    # Assert
    # with pytest.raises(IOError):
    #     valid_write = False
    #
    # assert result == expected

#
# FUNCTION      :   test_convert_ext()
# DESCRIPTION   :   This function ensures the file's extension is changed according to its inputs
# PARAMETERS    :
# RETURNS       :
@pytest.mark.parametrize(
    "file_name, expected",
    [("Text.txt", "Text.crp"), ("AnotherText.crp", "AnotherText.txt")],
)
def test_convert_ext(file_name, expected, test_files_dir):
    # Arrange
    file_name = os.path.join(test_files_dir, file_name)

    # Act
    new_file = convert_ext(file_name)

    # Assert
    # If it fails to open the same file, its been renamed.
    try:
        file_obj = open_file(file_name)
    except OSError:
        assert True




def test_failed_write(mocker):
    """ This test expects that the program will raise an exception if the file cannot be written to. """

    # Arrange
    file = "file.txt"
    content = "test content"
    write_mock = mocker.patch('builtins.open', new=mocker.mock_open())

    # Act
    # ..allow exception to be raised.
    with pytest.raises(IOError) as exception:
        # TODO: Use a different function if desired.
        check_write(content, file)

    # Assert
    # ..that open is called.
    write_mock.assert_any_call(file, 'w')
    write_mock().write.assert_any_call(content)
    # ..that exception is raised.
    assert exception.type is IOError

