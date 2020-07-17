import platform
import sys
import constants

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


def arg_parser():
    print('Parsing Command line Argument...')


def main():
    # OS Check
    print("Verifying OS...")
    if osCheck() == constants.SYS_ERROR:
        sys.exit()
    # Cmd line parse
    arg_parser()


if __name__ == "__main__":
    main()
