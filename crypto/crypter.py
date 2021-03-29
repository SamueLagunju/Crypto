# PROJECT       :   Crypto
# FILE          :   crypter.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-19
# DESCRIPTION   :   This file contains the class Crypter. 

import os
from collections import namedtuple
from typing import List, Callable, Dict, Literal
from .strategy import Strategy, SeanStrategy, RubikStrategy
from . import fileio as _fileio

CrypterVariant = namedtuple(
    "CrypterVariant", ["read_func", "write_func", "strategy", "operation"]
)
ext_mapping = {
    ".txt": CrypterVariant(
        _fileio.read_text_file, _fileio.write_text_file, SeanStrategy, "encrypt"
    ),
    ".crp": CrypterVariant(
        _fileio.read_text_file, _fileio.write_text_file, SeanStrategy, "decrypt"
    ),
    ".jpg": CrypterVariant(
        _fileio.read_image, _fileio.write_image, RubikStrategy, "encrypt"
    ),
    ".cip": CrypterVariant(
        _fileio.read_image, _fileio.write_image, RubikStrategy, "decrypt"
    ),
}

#   NAME          :   CrypterFactory
#   PURPOSE       :   This class is used to create the appropriate Crypter class, given a file name.
#                     Defines an interface for creating an object, but let subclasses decide which class to instantiate.
class CrypterFactory:
    def __init__(self, mapping: Dict[str, CrypterVariant] = None):
        if mapping is None:
            mapping = ext_mapping

        self.mapping = mapping

    # FUNCTION      :   create(self,file)
    # DESCRIPTION   :   This function provides some default implementation of the factory method.
    # PARAMETERS    :   file_extension - The file extension of the file passed into the function
    # RETURNS       :   Returns a crypter object variant on the strategy.
    def create(self, file_extension : str):
        variant = self.mapping[file_extension]
        return Crypter(
            variant.strategy(), variant.read_func, variant.write_func, variant.operation
        )


#   NAME          :   Crypter
#   PURPOSE       :   The Crypter class has been created to
#                     encrypt or decrypt files.
class Crypter:
    def __init__(
        self,
        strategy: Strategy,
        read_func: Callable,
        write_func: Callable,
        operation: Literal["encrypt", "decrypt"],
    ):
        self.strategy = strategy
        self.read_func = read_func
        self.write_func = write_func
        self.operation = operation

    # FUNCTION      :   convert_ext
    # DESCRIPTION   :   This function converts the extension of a file
    # PARAMETERS    :   file_name        -   Name of file and its extension
    # RETURNS       :   new_file_name    -   Name of the file with its new extension
    def convert_ext(self, file_name: str) -> str:
        """ Consumes a file name and produces a new file name. """
        ext_pairs = self.strategy.get_supported_types()
        file_stem, file_extension = os.path.splitext(file_name)

        new_file_name = None
        for pair in ext_pairs:
            if file_extension in pair:
                if self.operation == "decrypt":
                    new_file_name = file_stem + pair.decrypted
                else:
                    new_file_name = file_stem + pair.encrypted

        if new_file_name is None:
            raise ValueError(
                f"Strategy {type(self.strategy)} does not support extension {file_extension}."
            )

        return new_file_name

    #
    # FUNCTION      :   execute
    # DESCRIPTION   :   This function executes the
    #                   encryption/decryption process based on the given file
    # PARAMETERS    :   file -  Name of file and its extension
    # RETURNS       :   N/A
    def execute(self, file: str):
        """ Encrypts or decrypts the given files. """

        print("Reading content from: {0}".format(file))
        file_stem, file_extension = os.path.splitext(file)
        strategy = self.strategy
        file_contents = self.read_func(file)

        if self.operation == "encrypt":
            print("Encrypting: {0}".format(file))
            return_text = strategy.encrypt(file_contents)
        else:
            print("Decrypting: {0}".format(file))
            return_text = strategy.decrypt(file_contents)

        new_file = self.convert_ext(file)
        # Write File contents
        self.write_func(new_file, return_text)
        print("New File: {0}".format(new_file))
