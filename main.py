 
# FILE:         __main__.py
# PROJECT:      crypto
# PROGRAMMER:   Samuel Lagunju
# DESCRIPTION:  This file is the main for the module
import os

import click
from crypto.crypter import Crypter, CrypterFactory
from crypto.fileio import validate_file


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
    valid_files = [file for file in all_files if validate_file(file)]

    if not valid_files:
        # TODO replace with click mandatory
        print("No argument detected")
        print("Exiting...")
        return

    crypter_factory = CrypterFactory()

    for file_name in valid_files:
        file_stem, file_extension = os.path.splitext(file_name)

        crypter = crypter_factory.create(file_extension)

        crypter.execute(file_name)


if __name__ == "__main__":
    main()

