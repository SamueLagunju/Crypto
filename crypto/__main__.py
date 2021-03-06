# FILE:         __main__.py
# PROJECT:      crypto
# PROGRAMMER:   Samuel Lagunju
# DESCRIPTION:  This file is the main for the module


import sys
import click
from crypter import Crypter
from strategy import SeanStrategy
from fileio import read_file, write_file, validate_file, check_write


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
    decryption_extension = ["crp", "cip", "cpc"]
    encryption_extension = ["txt", "doc", "pdf"]
    output_text=''

    # If there are files to be decrypted
    if decrypt:
        for file_name in decrypt:
            if validate_file(file_name):
                # If the user's input is valid, process with encryption
                print("Decrypting: {0}".format(file_name))
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
    elif encrypt:
        for file_name in encrypt:
            # If the user's input is valid, process with encryption
            if validate_file(file_name):
                # If the user's input is valid, process with encryption
                print("Encrypting: {0}".format(file_name))
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

    # NEW - File encryption based on its extension
    elif files:
        for file in files:
filename, file_extension = os.path.splitext(file)
            crypter = Crypter(filename, SeanStrategy())
            file_contents = read_file(file)
            if file_extension in decryption_extension:
                print("Decrypting: {0}".format(file))
                output_text = crypter.decrypt_txt(file_contents)
            if file_extension in encryption_extension:
                print("Encrypting: {0}".format(file))
                output_text = crypter.encrypt_txt(file_contents)
            new_file_name = crypter.convert_ext(filename, file_extension)
            write_file(new_file_name, output_text)
            check_write(output_text, new_file_name)
            print("Output File: {0}".format(new_file_name))
    else:
        print("No argument detected")
        print("Exiting...")

if __name__ == "__main__":
    main()
