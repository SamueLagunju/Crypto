# PROJECT       :   Crypto
# FILE          :   crypter.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-19
# DESCRIPTION   :   This file contains the class Crypter.

import sys
import os
from strategy import SeanStrategy
from fileio import read_file, write_file, check_write

#   NAME          :   Crypter
#   PURPOSE       :   The Crypter class has been created to
#                     accurately extends the behavior of a Strategy pattern
#                     It is an interface of interest for encrypting/decrypting
class Crypter:

    def __init__(self):
        pass

    def execute(self, files):
        decryption_extension = [".crp", ".cip", ".cpc"]
        encryption_extension = [".txt", ".doc", ".pdf"]
        for file in files:
            print("Reading content from: {0}".format(file))
            file_contents = read_file(file)
            filename, file_extension = os.path.splitext(file)
            if file_extension in decryption_extension:
                print("Decrypting: {0}".format(file))
            if file_extension in encryption_extension:
                print("Encrypting: {0}".format(file))