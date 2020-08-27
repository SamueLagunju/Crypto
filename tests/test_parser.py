from crypto.helpers import arg_parser


import pytest


@pytest.mark.parametrize(
    "input,expected",
    [
        (["--encrypt", "file.txt"], ["file.txt"]),
        (["--encrypt", "test.txt"], ["test.txt"]),
        (["-e", "file.txt"], ["file.txt"]),
        (["-e", "test.txt"], ["test.txt"]),
    ],
)
def test_encrypt(input, expected):
    # Arrange
    parser = arg_parser

    # Act
    result = parser(input)

    # Assert
    assert result.encrypt_file == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        (["file.txt"], [["file.txt"]]),
        (["test.txt"], [["test.txt"]]),
    ],
)
def test_encrypt_implicit(input, expected):
    # Arrange
    parser = arg_parser

    # Act
    result = parser(input)

    # Assert
    assert result.Filename == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        (["--decrypt", "file.txt"], ["file.txt"]),
        (["--decrypt", "test.txt"], ["test.txt"]),
        (["-d", "file.txt"], ["file.txt"]),
        (["-d", "test.txt"], ["test.txt"]),
    ],
)
def test_decrypt(input, expected):
    # Arrange
    parser = arg_parser

    # Act
    result = parser(input)

    # Assert
    assert result.decrypt_file == expected
