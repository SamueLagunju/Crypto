 
# FILE:         __main__.py
# PROJECT:      crypto
# PROGRAMMER:   Samuel Lagunju
# DESCRIPTION:  This file is the main for the module
import os

import click
from crypto.crypter import Crypter, CrypterFactory
from crypto.fileio import validate_file, file_deconstruct


@click.command()
@click.option(
    "--encrypt", "-e", multiple=True, default="", help="Produces an encrypted file\n"
)
@click.option(
    "--decrypt", "-d", multiple=True, default="", help="Produces a decrypted file\n"
)
@click.argument("files", nargs=-1, type=click.Path())
def main(encrypt, decrypt, files):
    all_files = [*encrypt, *decrypt, *files]
    valid_files = [file for file in all_files if validate_file(file) == True]
    invalid_files = [file for file in all_files if (validate_file(file) == False)]

    if valid_files:
        crypter_factory = CrypterFactory()
        file_stems, file_extensions, file_names =  file_deconstruct(valid_files)
        crypter_ojects = crypter_factory.create(file_extensions)
        for crypter_ojects, file_names in zip(crypter_ojects, file_names):
            crypter_ojects.execute(file_names)

    if invalid_files:
        for invalid_file in invalid_files:
            print("Invalid File: {0}".format(invalid_file))

    print("Exiting...")
if __name__ == "__main__":
    main()
