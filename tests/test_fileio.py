"""
* Project Name: Crypto
* File Name: test_fileio.py
* Programmer: Kai Prince
* Date: Thu, Aug 06, 2020
* Description: This file contains tests for the FileIO functions.
"""
import pytest
from crypto.fileio import read_file


@pytest.mark.skip("TODO")
@pytest.mark.parametrize("input,expected", [("read1.txt", "abcdef")])
def test_read_file(input, expected):
    # Arrange

    # Act
    result = read_file(input)

    # Assert
    assert result == expected

