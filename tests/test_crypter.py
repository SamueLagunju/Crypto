"""
* Project Name: Crypto
* File Name: test_crypter.py
* Programmer: Kai Prince
* Date: Tue, Mar 23, 2021
* Description: This file contains tests for the Crypter class.
"""
import pytest
from pytest_mock import MockFixture

from crypto.crypter import Crypter
from crypto.strategy import ExtPair, SeanStrategy


def test_make_crypter():
    """ Makes an instance of the Crypter class. """
    # Arrange

    # Act
    crypter = Crypter()

    # Assert
    assert isinstance(crypter, Crypter)


def test_encrypt_file_contents(mocker: MockFixture):
    """ Encrypts file contents using a strategy. """
    # Arrange
    contents = "this is a string"
    # ..mock Strategy
    mock_strategy = mocker.MagicMock()
    mock_strategy.get_supported_types.return_value = [ExtPair(".txt", ".crp")]
    # ..mock fileio
    mock_file_reader = mocker.MagicMock()
    mock_file_reader.read_file.return_value = contents
    # ..make crypter
    crypter = Crypter(strategy_factory=lambda: [mock_strategy], fileio=mock_file_reader)

    # Act
    crypter.execute(["test.txt"])

    # Assert
    assert mock_strategy.encrypt.called_once_with(contents)


@pytest.mark.parametrize(
    "file_name, expected",
    [("Text.txt", "Text.crp"), ("AnotherText.crp", "AnotherText.txt")],
)
def test_convert_ext(file_name, expected):
    #
    # FUNCTION      :   test_convert_ext()
    # DESCRIPTION   :   This function ensures the file's extension is changed
    #                   according to its inputs
    # PARAMETERS    :
    # RETURNS       :

    # Arrange
    crypter = Crypter()

    # Act
    new_file = crypter.convert_ext(SeanStrategy(), file_name)

    # Assert
    # ..that the new file name is correct
    assert new_file == expected
