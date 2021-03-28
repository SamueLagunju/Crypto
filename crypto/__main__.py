# FILE:         __main__.py
# PROJECT:      crypto
# PROGRAMMER:   Samuel Lagunju
# DESCRIPTION:  This file is the main for the module


import click
from crypter import Crypter
from fileio import validate_file


@click.command()
@click.option(
    "--encrypt", "-e", multiple=True, default="", help="Produces an encrypted file\n"
)
@click.option(
    "--decrypt", "-d", multiple=True, default="", help="Produces a decrypted file\n"
)
@click.argument("files", nargs=-1, type=click.Path())
def main(encrypt, decrypt, files):
    # Not completely sure I might need to implement.
    # program_directory = Path().resolve()
    # program_os = os_checker()
    # if not program_os:
    #     sys.exit(SYS_ERROR)
    all_files = [*encrypt, *decrypt, *files]
    valid_files = [file for file in all_files if validate_file(file)]

    if not valid_files:
        # TODO replace with click mandatory
        print("No argument detected")
        print("Exiting...")
        return

    crypter = Crypter()
    crypter.execute(valid_files)


if __name__ == "__main__":
    main()
