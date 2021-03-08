# PROJECT       :   Crypto
# FILE          :   crypter.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-19
# DESCRIPTION   :   This file contains the class Crypter.

import sys
import os
from typing import List, Tuple

from strategy import SeanStrategy, Strategy, RubikStrategy, DocStrategy
from fileio import read_file, write_file, check_write


#   NAME          :   Crypter
#   PURPOSE       :   The Crypter class has been created to
#                     accurately extends the behavior of a Strategy pattern
#                     It is an interface of interest for encrypting/decrypting
class Crypter:

    strategies: List[Strategy]

    def __init__(self):
        self.strategies = self.make_strategies()

    @staticmethod
    def make_strategies() -> List[Strategy]:
        """ Factory function that creates all the Strategies. """
        strategies = [SeanStrategy(), RubikStrategy(), DocStrategy()]

        return strategies

    @staticmethod
    def should_encrypt(strategy: Strategy, ext: str) -> bool:
        types = strategy.get_supported_types()

        for extensions in types:
            if ext in extensions:
                return ext == extensions.encrypted

        return False

    def get_strategy(self, ext: str) -> Strategy:
        """ Returns the first strategy the supports the given type. """
        for strategy in self.strategies:
            if ext in strategy.get_supported_types():
                return strategy

    def whichExtension(self, strategy: Strategy, file_name):
        extPair = strategy.get_supported_types()

        if self.should_encrypt:
            # new_file = file_name +

    def execute(self, files):
        for file in files:
            print("Reading content from: {0}".format(file))
            file_contents = read_file(file)
            filename, file_extension = os.path.splitext(file)

            strategy = self.get_strategy(file_extension)

            if self.should_encrypt(strategy, file_extension):
                print("Encrypting: {0}".format(file))
                strategy.encrypt(file_contents)
            else:
                print("Decrypting: {0}".format(file))
                strategy.decrypt(file_contents)
