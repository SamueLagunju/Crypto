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




def main():
    # Cmd line parse
    options = arg_parser(sys.argv[1:])
    # OS Check
    print("Verifying OS...")
    if osCheck() == constants.SYS_ERROR:
        sys.exit()

    if options.encrypt_file:
        print(f'Encryption File: {options.encrypt_file}')
    if options.decrypt_file:
        print(f'Decryption File: {options.decrypt_file}')


if __name__ == "__main__":
    main()
