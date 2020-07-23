import platform
from pathlib import Path
import argparse
from .constants import *
import sys


#   FUNCTION:       validate_file
#   DESCRIPTION:    Checking if a file exists
#   PARAMETERS:     file - file inputted from command line arg
#   RETURNS:        If the file does not exist, the function raises an error
def validate_file(file):
    config = Path(file)
    if not config.is_file():
        raise argparse.ArgumentTypeError("Could not find: {0}".format(file))


#   FUNCTION:       osCheck()
#   DESCRIPTION:    Checks which operating system its being run on
#   PARAMETERS:     N/A
#   RETURNS:        SYS_ERROR - If it cannot detect an OS
def osCheck():
    # OS Check
    print("Verifying OS...")
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
        return SYS_ERROR


def arg_parser(args=sys.argv[1:]):
    print('Parsing Command line Argument...')

    parser = argparse.ArgumentParser(prog=sys.argv[0], description="An encrypting / decrypting utility for Linux.\n")
    parser.add_argument('-e', '--encrypt', metavar='Encryption file', action='append', type=validate_file,
                        dest='encrypt_file', help="Produces an encrypted file\n")
    parser.add_argument('-d', '--decrypt', metavar='Decryption file', action='append', type=validate_file,
                        dest='decrypt_file', help="Produces a decrypted file\n")
    parser.add_argument('Filename', metavar='No-switch file', nargs='?',  type=str,
                         help="Produces an encrypted file\n")
    options = parser.parse_args(args)
    return options
