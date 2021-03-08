# PROJECT       :   Crypto
# FILE          :   strategy.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-20
# DESCRIPTION   :   The functions in this file are used to support the strategy interface interface


import abc


#
#   NAME          :   Strategy
#   PURPOSE       :   The Strategy class declares operations common to all supported versions
#                     of some algorithm.
from typing import List, Tuple
from collections import namedtuple

ExtPair = namedtuple("ExtPair", ["encrypted", "decrypted"])


class Strategy(abc.ABC):

    @abc.abstractmethod
    def get_supported_types(self) -> List[ExtPair]:
        pass

    @abc.abstractmethod
    def encrypt_text(self, input_text):
        pass

    @abc.abstractmethod
    def decrypt_text(self, cipher_text):
        pass


#
#   NAME          :   SeanStrategy
#   PURPOSE       :   The SeanStrategy class implement the algorithms while following
#                     the base strategy interface. The interface makes them interchangeable in the context.
#                     Concrete strategy for Sean Clarke's encryption scheme.
class SeanStrategy(Strategy):

    def encrypt(self, data: bytes):
        """ Convert to plain text, then call inner function. """
        plain_text = data.decode("utf-8")
        return self.encrypt_text(plain_text)

    # METHOD        :   encrypt_text
    # DESCRIPTION   :   This function translate the ASCII value of the
    #                   new encrypted character to a 2 digit hexadecimal value.
    # PARAMETERS    :   plain_text  -   Text that is about to be encrypted into cipher text
    # RETURNS       :   cipher_text -   2 digit hexadecimal value

    def encrypt_text(self, plain_text):
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

    def decrypt(self, data: bytes):
        """ Convert to plain text, then call inner function. """
        cipher_text = data.decode("ascii")
        return self.decrypt_text(cipher_text)
        pass

    # METHOD        :   decrypt_text
    # DESCRIPTION   :   This function translates a 2 digit hexadecimal
    #                   value to a decoded ASCII value
    # PARAMETERS    :   cipher_text  -   Text that is about to be decrypted into plain text
    # RETURNS       :   plain_text   -   ASCII value
    def decrypt_text(self, cipher_text):
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

    # FUNCTION      :   convert_ext
    # DESCRIPTION   :   This function converts the extension of a file
    # PARAMETERS    :   file        -   Name of file and its extension
    # RETURNS       :   new_file    -   Name of the file with its new extension
    def convert_ext(self, file_name, old_ext):
        if old_ext == "txt":
            new_file = file_name + ".crp"
        elif old_ext == "crp":
            new_file = file_name + ".txt"
        return new_file

