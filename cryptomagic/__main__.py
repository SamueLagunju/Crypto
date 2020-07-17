import platform
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
    # parser = argparse.ArgumentParser()
    #
    # parser.add_argument('-e', '--encrypt', action='store_true',
    #                     help="Produces an encrypted file", dest='encryption_file')
    # parser.add_argument('-d', '--decrypt', action='store_true',
    #                     help="Produces a decrypted file")
    #
    # args = parser.parse_args()
    #
    # # If encrypt is detected
    # if args.encrypt:
    #     print(f'Encryption File: {args.encryption_file}')
    # # If encrypt is detected
    # elif args.decrypt:
    #     print(f'Decryption File: {args.decrypt}')
    # else:
    #     print("Default Mode: Encryption.")
    parser = argparse.ArgumentParser(description="An encrypting / decrypting utility for Linux.")
    parser.add_argument('-e', '--encrypt', dest='encrypt_file',
                        help="Produces an encrypted file")
    parser.add_argument('-d', '--decrypt',  dest='decrypt_file',
                        help="Produces a decrypted file")
    parser.add_argument("-n", "--number", type=int, help="A number.")


    # parser.add_argument('-e', '--encrypt', action='store_true',
    #                     help="Produces an encrypted file", dest='encryption_file')
    # parser.add_argument('-d', '--decrypt', action='store_true',
    #                     help="Produces a decrypted file")
    options = parser.parse_args(args)
    return options

def main():
    # OS Check
    print("Verifying OS...")
    if osCheck() == constants.SYS_ERROR:
        sys.exit()

    # Cmd line parse
    options = arg_parser(sys.argv[1:])
    print(f'Encryption File: {options.encrypt_file}')
    print(f'Encryption File: {options.decrypt_file}')


if __name__ == "__main__":
    main()
