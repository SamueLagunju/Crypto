#
# FILE:        constants.py
# PROJECT:      CryptoMagic
# PROGRAMMER:   Samuel Lagunju
# DESCRIPTION:  This file contains global constants.
#


class Crypter:
    def __init__(self, input_file):
        self.input_file = input_file

    def print_input_file(self):
        print(self.input_file)

    #


class Encrypter(Crypter):
    def __init__(self, output_file, input_file):
        super().__init__(input_file)
        self.output_file = output_file

    def print_output_file(self):
        print(self.output_file)

    def encrypt_txt(self, plain_text):
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
                    cipher_text += 'TT'
                # Apply encryption scheme
                else:
                    # Taking the ASCII code for the input character and subtracting a value of 16 from it
                    cipher_char = ascii_plain_text - 16
                    # If the resulting outChar value is less than 32, another step must be taken:
                    if cipher_char < 32:
                        cipher_char = (cipher_char - 32) + 144
                    # Transforming result to 2 digit hexadecimal value
                    cipher_text += format(cipher_char, 'X')
        return cipher_text


class Decrypter(Crypter):
    def __init__(self, output_file, input_file):
        super().__init__(input_file)
        self.output_file = output_file

    def print_output_file(self):
        print(self.output_file)
