# PROJECT       :   Crypto
# FILE          :   fileio.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-07
# DESCRIPTION   :   The functions in this file are used to

import os

available_extensions = [".txt", ".pdf"]


def open_file(new_input):
    obj_file = open(new_input, "r")
    return obj_file


def read_file(input_file):
    file_buffer = ""
    with open(input_file, "r") as file_pointer:
        for cnt, line in enumerate(file_pointer):
            file_buffer += line
    return file_buffer


def write_file(output_file, content):
    with open(output_file, "w") as file_pointer:
        file_pointer.write(content)


#   FUNCTION:       validate_file
#   DESCRIPTION:    Checking if a file exists
#                   Also checks if the file exists with other extensions
#   PARAMETERS:     File            -  Input file
#   RETURNS:        valid_status    -  If the file exist, it returns true
#                                      If the file does not exist, it returns false
def validate_file(file):
    valid_status = False
    file_name, ext = os.path.splitext(file)
    # THIS IS AN IDEA FOR ANOTHER TIME -
    # YOU NEED TO CREATE A NEW INPUT with an 'accepted' extension
    # # If there is not an extension, try and open it with a set of extensions
    # if not ext:
    #     for curr_test_extension in available_extensions:
    #         valid_status = os.path.exists(file_name + curr_test_extension)
    #         if valid_status:
    #             break
    if ext:
        valid_status = os.path.exists(file)
    return valid_status


def check_write(file_buffer, file):
    # Write to the file first
    write_file(file, file_buffer)

    # Open the written file
    file_content = read_file(file)

    # Compare file content with file_buffer
    if file_buffer != file_content:
        raise IOError


def convert_ext(file):
    file_name, ext = os.path.splitext(file)
    if ext == ".txt":
        new_file = file_name + '.crp'
        os.rename(file, new_file)
    elif ext == ".crp":
        new_file = file_name + '.txt'
        os.rename(file, new_file)
    return new_file
