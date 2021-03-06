# FILE:         __main__.py
# PROJECT:      crypto
# PROGRAMMER:   Samuel Lagunju
# DESCRIPTION:  This file is the main for the module


import click
from crypter import Crypter
from fileio import validate_file


@click.command()
@click.option('--encrypt', '-e', multiple=True, default='', help="Produces an encrypted file\n")
@click.option('--decrypt', '-d', multiple=True, default='', help="Produces a decrypted file\n")
@click.argument('files', nargs=-1, type=click.Path())
def main(encrypt, decrypt, files):
    # Not completely sure I might need to implement.
    # program_directory = Path().resolve()
    # program_os = os_checker()
    # if not program_os:
    #     sys.exit(SYS_ERROR)
    list_of_files = []
    rules = [encrypt,
             decrypt,
             files]
    # If there are files
    if any(rules):
        for element in rules:
            if element:
                for file in element:
                    if validate_file(file):
                        list_of_files.append(file)

        crypter = Crypter()
        crypter.execute(list_of_files)
    else:
        print("No argument detected")
        print("Exiting...")


if __name__ == "__main__":
    main()
