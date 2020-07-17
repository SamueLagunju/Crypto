import platform


def osCheck():
    if platform.system() == "linux":
        print('Linux OS detected')
    elif platform.system() == "darwin":
        print('Mac OS detected')
    elif platform.system() == "Windows":
        print('Windows OS detected')


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
