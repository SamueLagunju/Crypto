# PROJECT       :   Crypto
# FILE          :   helpers.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-07
# DESCRIPTION   :   The functions in this file are miscellaneous

import platform
import argparse
import sys


#   FUNCTION:       osCheck()
#   DESCRIPTION:    Checks which operating system its being run on
#   PARAMETERS:     N/A
#   RETURNS:        plt         -   Name of platform that was detected
#                   SYS_ERROR   -   Raised an error if it cannot detect an OS


def os_checker():
    # OS Check
    print("Verifying OS...")
    plt = platform.system()
    if plt == "Windows":
        print("Windows OS detected")
    elif plt == "Linux":
        print("Linux OS detected")
    elif plt == "Darwin":
        print("Mac OS detected")
    else:
        print("Unidentified system")
        raise SystemError
    return plt


#
# FUNCTION      :   arg_parser
# DESCRIPTION   :   This function parses arguments inputted by the user and returns it as a list
# PARAMETERS    :   sys.argv[1:]    -   A list of strings representing the arguments
#                                       (as separated by spaces) on the command-line
# RETURNS       :   options         -   A parser object
def arg_parser(args=sys.argv[1:]):
    print("Parsing Command line Argument...")

    parser = argparse.ArgumentParser(
        prog=sys.argv[0], description="An encrypting / decrypting utility for Linux.\n"
    )
    parser.add_argument(
        "-e",
        "--encrypt",
        metavar="Encryption file",
        action="append",
        dest="encrypt_file",
        help="Produces an encrypted file\n",
    )
    parser.add_argument(
        "-d",
        "--decrypt",
        metavar="Decryption file",
        action="append",
        dest="decrypt_file",
        help="Produces a decrypted file\n",
    )
    parser.add_argument(
        "Filename",
        metavar="File.txt",
        nargs="*",
        action="append",
        help="Produces an encrypted file\n",
    )
    options = parser.parse_args(args)
    return options
