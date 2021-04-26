# PROJECT       :   Crypto
# FILE          :   strategy.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-20
# DESCRIPTION   :   The functions in this file are used to support the strategy interface interface


import abc
from PIL import Image
import random
from .constants import image_key
from typing import List, Tuple, Callable, Any
from collections import namedtuple

ExtPair = namedtuple("ExtPair", ["decrypted", "encrypted"])


class Strategy(abc.ABC):
    """
    NAME          :   Strategy
    PURPOSE       :   The Strategy class accurately extends the behavior
                      of a Strategy pattern.

                      It is an interface of interest for encrypting/decrypting
                      file contents.
    """

    @staticmethod
    @abc.abstractmethod
    def get_supported_types() -> List[ExtPair]:
        pass

    @abc.abstractmethod
    def encrypt(self, data):
        pass

    @abc.abstractmethod
    def decrypt(self, data):
        pass

    #


#   NAME          :   SeanStrategy
#   PURPOSE       :   The SeanStrategy class implement the algorithms while following
#                     the base strategy interface. The interface makes them interchangeable in the context.
#                     Concrete strategy for Sean Clarke's encryption scheme.
class SeanStrategy(Strategy):
    def encrypt(self, file_contents):
        """ Call inner function. """
        return self.encrypt_text(file_contents)

    # METHOD        :   encrypt_text
    # DESCRIPTION   :   This function translate the ASCII value of the
    #                   new encrypted character to a 2 digit hexadecimal value.
    # PARAMETERS    :   plain_text  -   Text that is about to be encrypted into cipher text
    # RETURNS       :   cipher_text -   2 digit hexadecimal value
    @staticmethod
    def encrypt_text(plain_text: str):
        cipher_text = ""
        # Transversing the string using range function
        for pt_char_index in range(len(plain_text)):
            if "\n" in plain_text[pt_char_index]:
                cipher_text += plain_text[pt_char_index]
            else:
                # Returning plain text into integer
                ascii_plain_text = ord(plain_text[pt_char_index])
                # If the character is a <tab> (ASCII value 9) it is just TT
                if ascii_plain_text == 9:
                    cipher_text += "TT"
                # Apply encryption scheme
                else:
                    # Taking the ASCII code for the input character and subtracting a
                    # value of 16 from it
                    cipher_char = ascii_plain_text - 16
                    # If the resulting outChar value is less than 32, another step must
                    # be taken:
                    if cipher_char < 32:
                        cipher_char = (cipher_char - 32) + 144
                    # Transforming result to 2 digit hexadecimal value
                    cipher_text += format(cipher_char, "X")

        return cipher_text

    def decrypt(self, file_contents: str):
        """ Call inner function. """
        return self.decrypt_text(file_contents)

    # METHOD        :   decrypt_text
    # DESCRIPTION   :   This function translates a 2 digit hexadecimal
    #                   value to a decoded ASCII value
    # PARAMETERS    :   cipher_text  -   Text that is about to be decrypted into plain text
    # RETURNS       :   plain_text   -   ASCII value
    @staticmethod
    def decrypt_text(cipher_text: str):
        plain_text = ""
        n = 2
        # Parsing the cipher text, line by line
        for cipher_line in cipher_text.splitlines():
            # Parsing each line and decrypting the file
            for index in range(0, len(cipher_line), n):
                # Capturing each pair of characters in the input line
                char_pair = cipher_line[index : index + n]
                # If the pair of characters is the sequence TT it simply transforms
                # into a <tab> character
                if char_pair == "TT":
                    plain_text += "\t"
                else:
                    # Converting from hex to decimal and adding 16
                    plain_char = int(char_pair, 16) + 16
                    # If the resulting outChar value is greater than 127, then another
                    # step is taken
                    if plain_char > 127:
                        plain_char = (plain_char - 144) + 32
                    plain_text += chr(plain_char)

            # Adding the new line character back to the line
            plain_text += "\n"
        return plain_text

    @staticmethod
    def get_supported_types() -> List[ExtPair]:
        return [ExtPair(".txt", ".crp")]


#
#   NAME          :   RubikStrategy
#   PURPOSE       :   The RubikStrategy class implement the algorithms while following
#                     the base strategy interface. The interface makes them interchangeable in the context.
class RubikStrategy(Strategy):

    def encrypt(self, file):
        """ Call inner function. """
        return self.encrypt_image(file)

    def decrypt(self, file):
        return self.decrypt_image(file)

    def get_supported_types(self) -> List[ExtPair]:
        return [ExtPair(".jpg", ".cip")]

    # METHOD        :
    # DESCRIPTION   :
    # PARAMETERS    :
    # RETURNS       :
    def encrypt_image(self, img: bytes):
        numericData = bytearray(img)
        self.xor_operator(numericData, img)
        return numericData

    # METHOD        :
    # DESCRIPTION   :
    # PARAMETERS    :
    # RETURNS       :
    def decrypt_image(self, img: bytes):
        numericData = bytearray(img)
        self.xor_operator(numericData, img)
        return numericData

    # METHOD        :
    # DESCRIPTION   :
    # PARAMETERS    :
    # RETURNS       :
    def xor_operator(self, data: bytearray, img_data: bytes):
        for index, values in enumerate(img_data):
            data[index] = values ^ image_key

#
#   NAME          :   DocStrategy
#   PURPOSE       :   The DocStrategy class implement the algorithms while following
#                     the base strategy interface. The interface makes them interchangeable in the context.
class DocStrategy(Strategy):
    def get_supported_types(self) -> List[ExtPair]:
        return [ExtPair(".doc", ".cop"), ExtPair(".pdf", ".cpc")]

    def encrypt(self, data: bytes):
        raise NotImplemented

    def decrypt(self, data: bytes):
        raise NotImplemented
