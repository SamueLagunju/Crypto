import platform


def osCheck():
    plt = platform.system()
    if plt == "Windows":
        print("Your system is Windows")
        # do x y z
    elif plt == "Linux":
        print("Your system is Linux")
        # do x y z
    elif plt == "Darwin":
        print("Your system is MacOS")
        # do x y z
    else:
        print("Unidentified system")


def arg_parser():
    print('Parsing Command line Argument...')


def main():
    # OS Check
    print("Verifying OS...")
    osCheck()
    # Cmd line parse
    arg_parser()


if __name__ == "__main__":
    main()
