import pytest

from crypto.strategy import SeanStrategy, RubikStrategy
from crypto.constants import image_key


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
                    "3D69805E515D55805963804355515E80335C51625B558ETT398"
                    "05C595B5580635F56646751625581\n"
                ),
            ),
        ],
    )
    def test_encrypt_string(self, input, expected):
        # Arrange
        client = SeanStrategy()

        # Act
        result = client.encrypt(input)

        # Assert
        assert result == expected

    @pytest.mark.parametrize(
        "input,expected",
        [
            ("515253545556\n", "abcdef\n"),
            (
                (
                    "4458596380555E5362696064595F5E806353"
                    "58555D55805963806062556464698067555962548E\n"
                    "39635E87648059642F812F\n"
                ),
                ("This encryption scheme is pretty weird.\nIsn't it?!?\n"),
            ),
        ],
    )
    def test_decrypt_string(self, input, expected):
        # Arrange
        client = SeanStrategy()

        # Act
        result = client.decrypt(input)

        # Assert
        assert result == expected


    @pytest.mark.parametrize(
        "input,expected",
        [
            (b'ADBCEFGH1', b'VSUTRQP_&'),
        ],
    )
    def test_image_encrypt(self, input, expected):
        # Arrange
        client = RubikStrategy()

        # Act
        result = client.encrypt(input)

        # Assert
        assert result == expected

    @pytest.mark.parametrize(
        "input,expected",
        [
            (b'VSUTRQP_&', b'ADBCEFGH1'),
        ],
    )
    def test_image_decrypt(self, input, expected):
        # Arrange
        client = RubikStrategy()

        # Act
        result = client.decrypt(input)

        # Assert
        assert result == expected
