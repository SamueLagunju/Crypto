# PROJECT       :   Crypto
# FILE          :   crypter.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-19
# DESCRIPTION   :   This file contains the class Crypter.

import os
from typing import List, Callable

from .helpers import make_strategies
from .strategy import Strategy
from . import fileio as _fileio


#   NAME          :   Crypter
#   PURPOSE       :   The Crypter class has been created to
#                     encrypt or decrypt files.
class Crypter:

    strategies: List[Strategy]

    def __init__(
        self,
        strategy_factory: Callable[[], List[Strategy]] = make_strategies,
        fileio=_fileio,
    ):
        self.strategies = strategy_factory()
        self.fileio = fileio

    @staticmethod
    def should_encrypt(strategy: Strategy, ext: str) -> bool:
        """Returns true if the provided file extension represents
        an encrypted file."""
        types = strategy.get_supported_types()

        for extensions in types:
            if ext in extensions:
                return ext == extensions.encrypted

        return False

    def get_strategy(self, ext: str) -> Strategy:
        """ Returns the first strategy that supports the given type. """
        for strategy in self.strategies:
            for ext_pair in strategy.get_supported_types():
                if ext in ext_pair:
                    return strategy

        raise ValueError(f"No strategy found that supports the ext '{ext}'")

    def convert_ext(self, strategy: Strategy, file_name: str) -> str:
        """ Consumes a file name and produces a new file name. """
        ext_pairs = strategy.get_supported_types()
        file_stem, file_extension = os.path.splitext(file_name)

        new_file_name = None
        for pair in ext_pairs:
            if file_extension in pair:
                if self.should_encrypt(strategy, file_extension):
                    new_file_name = file_stem + pair.encrypted
                else:
                    new_file_name = file_stem + pair.decrypted

        if new_file_name is None:
            raise ValueError(
                f"Strategy {type(strategy)} does not support extension {file_extension}."
            )

        return new_file_name

    def execute(self, files: List[str]):
        """ Encrypts or decrypts the given files. """

        for file in files:
            print("Reading content from: {0}".format(file))
            file_contents = self.fileio.read_file(file)
            file_stem, file_extension = os.path.splitext(file)

            strategy = self.get_strategy(file_extension)

            if self.should_encrypt(strategy, file_extension):
                print("Encrypting: {0}".format(file))
                strategy.encrypt(file_contents)
            else:
                print("Decrypting: {0}".format(file))
                strategy.decrypt(file_contents)
