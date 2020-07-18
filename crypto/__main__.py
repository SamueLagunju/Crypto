import platform
import os
import sys
import constants
import argparse


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


def arg_parser(args=sys.argv[1:]):
    print('Parsing Command line Argument...')

    parser = argparse.ArgumentParser(prog=sys.argv[0], description="An encrypting / decrypting utility for Linux.\n")
    parser.add_argument('-e', '--encrypt', metavar='Encryption file', action='append',
                        dest='encrypt_file', help="Produces an encrypted file\n")
    parser.add_argument('-d', '--decrypt', metavar='Decryption file', action='append',
                        dest='decrypt_file', help="Produces a decrypted file\n")
    options = parser.parse_args(args)
    return options


def seans_encryption(plain_text):
    print('Encrypting...Low Mode...')
    cipher_text = ""
    # Transversing the string using range function
    for pt_char_index in range(len(plain_text)):
        ascii_plain_text = ord(plain_text[pt_char_index])
        # If the character is a <tab> (ASCII value 9) it is just TT
        if ascii_plain_text == 9:
            cipher_text += 'TT'
        # Apply encryption scheme
        else:
            # Taking the ASCII code for the input character and subtracting a value of 16 from it
            cipher_char = ascii_plain_text - 16
            if cipher_char < 32: # If the resulting outChar value is less than 32, another step must be taken:
                cipher_char = (cipher_char -32) + 144
            # Transforming result to 2 digit hexadecimal value
            cipher_text += format(cipher_char, 'X')

    print(cipher_text)

def seans_decryption(plain_text):
    pass

def main():
    # Cmd line parse
    options = arg_parser(sys.argv[1:])
    # OS Check
    print("Verifying OS...")
    if osCheck() == constants.SYS_ERROR:
        sys.exit()

    if options.encrypt_file:
        print(f'Encryption File: {options.encrypt_file}\n')
        while True:
            plainText = input("Enter Text:")
            seans_encryption(plainText)
    if options.decrypt_file:
        print(f'Decryption File: {options.decrypt_file}')


if __name__ == "__main__":
    main()
