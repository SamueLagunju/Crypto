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
                cipher_char = (cipher_char -32) + 144
            # Transforming result to 2 digit hexadecimal value
            cipher_text += format(cipher_char, 'X')

    return cipher_text


def seans_decryption(cipher_text):
    print('Decrypting...Low Mode...')
    plain_text = ""
    # Transversing the string using range
    n = 2
    for index in range(0, len(cipher_text), n):
        char_pair = cipher_text[index: index + n]
        if char_pair == 'TT':
            plain_text += '\t'
        else:
            # Converting from hex to decimal and adding 16
            plain_char = int(char_pair, 16) + 16

            if plain_char > 127:
                plain_char = (plain_char - 144) + 32

            plain_text += chr(plain_char)


    return plain_text



def main():
    # Cmd line parse
    options = arg_parser(sys.argv[1:])
    # OS Check
    print("Verifying OS...")
    if osCheck() == constants.SYS_ERROR:
        sys.exit()

    # if options.encrypt_file:
    #     print(f'Encryption File: {options.encrypt_file}')
    #     while True:
    #         plainText = input("Enter Text:")
    #         plainText = seans_encryption(plainText)
    #         print(plainText)
    # if options.decrypt_file:
    #     print(f'Decryption File: {options.decrypt_file}')
    #     while True:
    #         cipherText = input("Enter Text:")
    #         seans_decryption(cipherText)
    while True:
        user_text = input("Enter Text:")
        user_text = seans_encryption(user_text)
        print('Encrypted Text: {}'.format(user_text))
        user_text = seans_decryption(user_text)
        print('Decrypted Text: {}'.format(user_text))



if __name__ == "__main__":
    main()
