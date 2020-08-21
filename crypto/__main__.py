# FILE:         __main__.py
# PROJECT:      crypto
# PROGRAMMER:   Samuel Lagunju
# DESCRIPTION:  This file is the main for the module


import sys
from crypter import Crypter
from strategy import SeanStrategy
from fileio import read_file, write_file, validate_file, check_write, convert_ext
from helpers import arg_parser


def main():
    # Not completely sure I might need to implement.
    # program_directory = Path().resolve()
    # program_os = os_checker()
    # if not program_os:
    #     sys.exit(SYS_ERROR)

    args = arg_parser(sys.argv[1:])

    # If there are files to be decrypted
    if args.decrypt_file:
        for file_name in args.decrypt_file:
            if validate_file(file_name):
                # If the user's input is valid, process with encryption
                print("Decrypting file: {0}".format(file_name))
                crypter = Crypter(file_name, SeanStrategy())
                # All FileIO operations
                try:
                    file_contents = read_file(file_name)
                    decrypted_text = crypter.decrypt_txt(file_contents)
                    write_file(file_name, decrypted_text)
                    check_write(decrypted_text, file_name)
                    new_file = convert_ext(file_name)
                    print("Decrypted File: {0}".format(new_file))
                except IOError:
                    print("Failed to write to: {0}".format(file_name))
            else:
                print("Input {0} was not a valid file.".format(file_name))

    # If there are files to be encrypted
    if args.encrypt_file:
        for file_name in args.encrypt_file:
            # If the user's input is valid, process with encryption
            if validate_file(file_name):
                # If the user's input is valid, process with encryption
                print("Encrypting file: {0}".format(file_name))
                crypter = Crypter(file_name, SeanStrategy())
                # All FileIO operations
                try:
                    file_contents = read_file(file_name)
                    encrypted_text = crypter.encrypt_txt(file_contents)
                    write_file(file_name, encrypted_text)
                    check_write(encrypted_text, file_name)
                    new_file = convert_ext(file_name)
                    print("Encrypted File: {0}".format(new_file))
                except IOError:
                    print("Failed to write to: {0}".format(file_name))
            else:
                print("Input {0} was not a valid file.".format(file_name))


if __name__ == '__main__':
    main()
