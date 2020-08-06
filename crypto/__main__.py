#
# FILE:         __main__.py
# PROJECT:      crypto
# PROGRAMMER:   Samuel Lagunju
# DESCRIPTION:  Runs the application...
#

from .helpers import *
from .crypter import *
from .strategy import SeanStrategy
from .fileio import read_file


def main():
    program_directory = Path().resolve()
    program_os = os_checker()
    if not program_os:
        sys.exit(SYS_ERROR)

    args = arg_parser(sys.argv[1:])
    if args.decrypt_file:
        for file_name in args.decrypt_file:
            print("Decrypting file: {0}".format(file_name))

            crypter = Crypter(file_name, SeanStrategy())
            file_contents = read_file(file_name)

            decrypted_text = crypter.decrypt_txt(file_contents)

            print(decrypted_text)
    if args.encrypt_file:
        for file_name in args.encrypt_file:
            print("Encrypting file: {0}".format(file_name))

            crypter = Crypter(file_name, SeanStrategy())
            file_contents = read_file(file_name)

            encrypted_text = crypter.encrypt_txt(file_contents)

            print(encrypted_text)

if __name__ == '__main__':
    main()