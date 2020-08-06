import platform
from pathlib import Path
import argparse
from .constants import *


# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class PotentialFileError(Error):
    """Raised when the input file might be invalid"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


#   FUNCTION:       validate_file
#   DESCRIPTION:    Checking if a file exists
#   PARAMETERS:     file - file inputted from command line arg
#   RETURNS:        If the file does not exist, the function raises an error
def validate_file(files, whatMode=encryptMode):
    file_name, ext = os.path.splitext(files)
    loop = True
    # If file has no extension, try to open the file with several extensions
    if ext:
        if not os.path.exists(files):
            # Argparse uses the ArgumentTypeError to give a rejection message like:
            # error: argument input: x does not exist
            raise argparse.ArgumentTypeError("Could not find: {0}".format(files))
        return files
    else:
        print("No extension detected...Will try to search in current directory")
        currentDirectory = Path().absolute()
        for current_test_extension in available_extensions:
            test_file = Path(currentDirectory, files).with_suffix(current_test_extension)
            try:
                f = open(test_file)
                print("{} is accessible".format(files))
                f.close()
                break
            except FileNotFoundError:
                print('{} does not exist in directory...'.format(test_file))



    # if not Path(file).exists():
    #     raise argparse.ArgumentTypeError("Could not find: {0}".format(file))
    # if not Path(file).exists():
    #     raise argparse.ArgumentTypeError("Could not find: {0}".format(file))
    # return file
    #
    # if not Path(file).is_file():
    #     raise argparse.ArgumentTypeError("Could not find: {0}".format(file))
    # return file
    # Getting current directory of script to find file


    # try:
    #
    #     f = open(file_name, 'r')
    # except OSError:
    #     print("Could not open/read file:", file_name)
    #     raise PotentialFileError
    # except PotentialFileError:
    #     if whatMode == 'Decrypt':
    #         print('Decrypt Switch detected')
    # # print(file)
    # return file_name


#   FUNCTION:       osCheck()
#   DESCRIPTION:    Checks which operating system its being run on
#   PARAMETERS:     N/A
#   RETURNS:        SYS_ERROR - If it cannot detect an OS
def os_checker():
    # OS Check
    print("Verifying OS...")
    plt = platform.system()
    if plt == "Windows":
        print('Windows OS detected')
    elif plt == "Linux":
        print('Linux OS detected')
    elif plt == "Darwin":
        print('Mac OS detected')
    else:
        print("Unidentified system")
        plt = SYS_ERROR

    return plt


def arg_parser(args=sys.argv[1:]):
    print('Parsing Command line Argument...')

    parser = argparse.ArgumentParser(prog=sys.argv[0], description="An encrypting / decrypting utility for Linux.\n")
    parser.add_argument('-e', '--encrypt', metavar='Encryption file', action='append', dest='encrypt_file', help="Produces an encrypted file\n")
    parser.add_argument('-d', '--decrypt', metavar='Decryption file', action='append', dest='decrypt_file', help="Produces a decrypted file\n")
    parser.add_argument('Filename', metavar='File.txt', nargs='*', action='append', help="Produces an encrypted file\n")
    options = parser.parse_args(args)
    return options
