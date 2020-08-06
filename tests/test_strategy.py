import pytest

from crypto.crypter import Crypter
from crypto.strategy import SeanStrategy

def test_encrypt_string():
    print("HI")
    # Arrange
    input = "abcdef"
    client = Crypter("", SeanStrategy())

    # Act
    result = client.encrypt_txt(input)

    # Assert
    print(result)
    assert result == "515253545556"

def test_decrypt_string():
    print("HI")
    # Arrange
    input = "515253545556"
    client = Crypter("", SeanStrategy())

    # Act
    result = client.decrypt_txt(input)

    # Assert
    print(result)
    assert result == "abcdef"