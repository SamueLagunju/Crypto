import pytest

from crypto.crypter import Crypter
from crypto.strategy import SeanStrategy


class TestSeanStrategy:
    """ Tests for the Sean Strategy. """

    @pytest.mark.parametrize(
        "input,expected",
        [
            ("abcdef", "515253545556"),
            (
                (
                    "Hello There how are you?\n"
                    "My name is Sean Clarke.\tI like software!\n"
                ),
                (
                    "38555C5C5F80445855625580585F678051625580695F652F\n"
                    "3D69805E515D55805963804355515E80335C51625B558ETT39805C595B5580635F56646751625581\n"
                ),
            ),
        ],
    )
    def test_encrypt_string(self, input, expected):
        # Arrange
        client = Crypter("", SeanStrategy())

        # Act
        result = client.encrypt_txt(input)

        # Assert
        assert result == expected

    @pytest.mark.parametrize(
        "input,expected",
        [
            ("515253545556\n", "abcdef\n"),
            (
                (
                    "4458596380555E5362696064595F5E80635358555D55805963806062556464698067555962548E\n"
                    "39635E87648059642F812F\n"
                ),
                ("This encryption scheme is pretty weird.\nIsn't it?!?\n"),
            ),
        ],
    )
    def test_decrypt_string(self, input, expected):
        # Arrange
        client = Crypter("", SeanStrategy())

        # Act
        result = client.decrypt_txt(input)

        # Assert
        assert result == expected
