import pytest

from crypto.crypter import Crypter
from crypto.strategy import SeanStrategy


class TestSeanStrategy:
    """ Tests for the Sean Strategy. """

    @pytest.mark.parametrize(
        "input,expected", [("abcdef", "515253545556"),],
    )
    def test_encrypt_string(self, input, expected):
        # Arrange
        client = Crypter("", SeanStrategy())

        # Act
        result = client.encrypt_txt(input)

        # Assert
        assert result == expected

    @pytest.mark.parametrize(
        "input,expected", [("515253545556", "abcdef"),],
    )
    def test_decrypt_string(self, input, expected):
        # Arrange
        client = Crypter("", SeanStrategy())

        # Act
        result = client.decrypt_txt(input)

        # Assert
        assert result == expected
