#
# FILE:         __main__.py
# PROJECT:      crypto
# PROGRAMMER:   Samuel Lagunju
# DESCRIPTION:  The functions in this file are used to …
#

import platform
import os
import sys
import constants
import argparse


#   FUNCTION:
#   DESCRIPTION:
#   PARAMETERS:
#   RETURNS:
def osCheck():
    plt = platform.system()

    if plt == "Windows":
        print('Windows OS detected')
        # do x y z
    elif plt == "Linux":
        print('Linux OS detected')
        # do x y z
    elif plt == "Darwin":
        print('Mac OS detected')
        # do x y z
    else:
        print("Unidentified system")
        return constants.SYS_ERROR


#   FUNCTION:
#   DESCRIPTION:
#   PARAMETERS:
#   RETURNS:
def arg_parser(args=sys.argv[1:]):
    print('Parsing Command line Argument...')

    parser = argparse.ArgumentParser(prog=sys.argv[0], description="An encrypting / decrypting utility for Linux.\n")
    parser.add_argument('-e', '--encrypt', metavar='Encryption file', action='append', type=validate_file,
                        dest='encrypt_file', help="Produces an encrypted file\n")
    parser.add_argument('-d', '--decrypt', metavar='Decryption file', action='append', type=validate_file,
                        dest='decrypt_file', help="Produces a decrypted file\n")
    options = parser.parse_args(args)
    return options


#   FUNCTION:
#   DESCRIPTION:
#   PARAMETERS:
#   RETURNS:
def seans_encryption(plain_text):
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


#   FUNCTION:
#   DESCRIPTION:
#   PARAMETERS:
#   RETURNS:
def seans_decryption(cipher_text):
    plain_text = ""
    # Transversing the string using range
    n = 2
    for index in range(0, len(cipher_text), n):
        # The carriage return characters are not decrypted.
        if "\n" in cipher_text[index]:
            plain_text += cipher_text[index]
        else:
            char_pair = cipher_text[index: index + n]
            # If the pair of characters is the sequence TT
            # Tt simply transforms into a <tab> character (ASCII value 9) in the output file.
            if char_pair == 'TT':
                plain_text += '\t'
            else:
                # Converting from hex to decimal and adding 16
                plain_char = int(char_pair, 16) + 16
                # If the resulting outChar value is greater than 127, then another step is taken
                if plain_char > 127:
                    plain_char = (plain_char - 144) + 32
                # Transforming result to a char
                plain_text += chr(plain_char)

    return plain_text


#   FUNCTION:
#   DESCRIPTION:
#   PARAMETERS:
#   RETURNS:
def validate_file(f):
    if not os.path.exists(f):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("Could not find: {0}".format(f))
    return f


#   FUNCTION:
#   DESCRIPTION:
#   PARAMETERS:
#   RETURNS:
def main():
    # Cmd line parse
    options = arg_parser(sys.argv[1:])
    # OS Check
    print("Verifying OS...")
    if osCheck() == constants.SYS_ERROR:
        sys.exit()
    file_buffer = ""
    if options.encrypt_file:
        print('Encrypting...Low Mode...')
        for file_index in options.encrypt_file:
            input_file = file_index
            print(f'Encryption File: {input_file}')
            with open(input_file, 'r') as file_pointer:
                for cnt, line in enumerate(file_pointer):
                    file_buffer += seans_encryption(line)

                # Testing write to file - WEIRD OUTPUT
                file_pointer.close()
                file_pointer = open(input_file, "w")
                file_pointer.write(file_buffer)
                file_pointer.close()
                os.rename(input_file, 'Woi.crp')
    if options.decrypt_file:
        print('Decrypting...Low Mode...')
        for file_index in options.decrypt_file:
            input_file = file_index
            print(f'Decryption File: {input_file}')
            with open(input_file, 'r') as file_pointer:
                for cnt, line in enumerate(file_pointer):
                    file_buffer += seans_decryption(line)

                file_pointer.close()
                file_pointer = open(input_file, "w")
                file_pointer.write(file_buffer)
                file_pointer.close()
                os.rename(input_file, 'Woi.txt')


if __name__ == "__main__":
    main()
