# TODO FHC
from crypto.crypter import Crypter, CrypterFactory, CrypterVariant
from crypto import strategy
from crypto import fileio
import pytest
import os


@pytest.mark.skip(reason="No way of currently testing this")
def test_crypter_factory():
    """ Creates the proper Crypter instance. """

    # Arrange
    mapping = {".txt": CrypterVariant(fileio.read_text_file, fileio.write_text_file, strategy.SeanStrategy, "encrypt")}

    # Act
    crypter = CrypterFactory(mapping).create(".txt")

    # Assert
    assert isinstance(crypter, Crypter)
    assert isinstance(crypter.strategy, strategy.SeanStrategy)
    assert crypter.read_func == fileio.read_text_file
    assert crypter.write_func == fileio.write_text_file



#
# FUNCTION      :   test_convert_ext()
# DESCRIPTION   :   This function ensures the file's extension is changed
#                   according to its inputs
# PARAMETERS    :
# RETURNS       :
@pytest.mark.skip(reason="No way of currently testing this")
@pytest.mark.parametrize(
    "file_name, expected",
    [("Text.txt", "Text.crp"), ("AnotherText.crp", "AnotherText.txt")],
)

@pytest.mark.skip(reason="No way of currently testing this")
def test_convert_ext(file_name, expected):
    # Arrange
    file_stem, file_extension = os.path.splitext(file_name)
    crypter = CrypterFactory().create(file_extension)

    # Act
    new_file = crypter.convert_ext(file_name)

    # Assert
    # ..that the new file name is correct
    assert new_file == expected
