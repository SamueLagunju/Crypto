from sys import platform as _platform


def osCheck():
    if _platform == "linux":
        print('Linux OS detected')
    elif _platform == "darwin":
        print('Mac OS detected')
    elif _platform == "Windows":
        print('Windows OS detected')
    else:
        return False


def arg_parser():
    print('Parsing Command line Argument...')


def main():
    # OS Check
    print("Verifying OS...")
    if not osCheck():
        exit(1)
    # Cmd line parse
    arg_parser()


if __name__ == "__main__":
    main()
