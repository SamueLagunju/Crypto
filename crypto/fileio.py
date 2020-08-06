# Contains FileIO functions

import os

def read_file(input_file):
    file_buffer = ""

    with open(input_file, 'r') as file_pointer:
        for cnt, line in enumerate(file_pointer):
            file_buffer += line

        file_pointer.close()
        # file_pointer = open(input_file, "w")
        # file_pointer.write(file_buffer)
        # file_pointer.close()

    return file_buffer