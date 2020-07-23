from .helpers import *


def main():
    run = Program()
    run.execute_program()


class Program:

    def execute_program(self):
        if osCheck():
            sys.exit(SYS_ERROR)
        options = arg_parser(sys.argv[1:])
        print(options)
