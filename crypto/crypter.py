# PROJECT       :   Crypto
# FILE          :   crypter.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-19
# DESCRIPTION   :   This file contains the class Crypter. 

import os
from collections import namedtuple
from typing import List, Callable, Dict, Literal

from .strategy import Strategy, SeanStrategy, RubikStrategy
from .constants import image_key

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
        _fileio.read_binary_file, _fileio.write_binary_file, RubikStrategy, "encrypt"
    ),
    ".cip": CrypterVariant(
        _fileio.read_binary_file, _fileio.write_binary_file, RubikStrategy, "decrypt"
    ),
}


#   NAME          :   CrypterFactory
#   PURPOSE       :   This class is used to create the appropriate Crypter class, given a file name.
#                     Produce families of related objects without specifying their concrete classes.
class CrypterFactory:
    def __init__(self, mapping: Dict[str, CrypterVariant] = None):
        if mapping is None:
            mapping = ext_mapping

        self.mapping = mapping

    def create(self, files):
        variants = []
        result = []
        for file in files:
            variants.append(self.mapping[file])

        for variant in variants:
            result.append(Crypter(variant.strategy(), variant.read_func, variant.write_func, variant.operation))
        return result


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

    def execute(self, file: str):
        """ Encrypts or decrypts the given files. """
        try:
            print("Reading content from: {0}".format(file))
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
        except FileNotFoundError:
            print("File does not exist")
