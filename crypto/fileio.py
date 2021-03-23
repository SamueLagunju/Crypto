# PROJECT       :   Crypto
# FILE          :   fileio.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-07
# DESCRIPTION   :   The functions in this file are used to

import os

available_extensions = [".txt", ".pdf"]

# FUNCTION      :   open_file
# DESCRIPTION   :   This function opens an existing file
# PARAMETERS    :   new_input   -   User input used to create a file object
# RETURNS       :   obj_file    -   A file object that contains methods and attributes
#                                   which latter can be used to retrieve information or
#                                   manipulate the file that was just opened
def open_file(new_input):
    obj_file = open(new_input, "r")
    return obj_file

# FUNCTION      :   read_file
# DESCRIPTION   :   This function reads an existing file and extract its content
# PARAMETERS    :   input_file  -   Input file used for reading
# RETURNS       :   file_buffer -   Content in the file, each line separated accordingly
def read_file(input_file):
    file_buffer = ""
    with open(input_file, "rb") as file_pointer:
        for cnt, line in enumerate(file_pointer):
            file_buffer += line
    return file_buffer


# FUNCTION      :   write_file
# DESCRIPTION   :   This function writes content to an existing file
# PARAMETERS    :   output_file -   Output file used for writing
#                   content     -   Content in the file, each line separated accordingly
# RETURNS       :   N/A
def write_file(output_file, content):
    with open(output_file, "w") as file_pointer:
        file_pointer.write(content)


#   FUNCTION:       validate_file
#   DESCRIPTION:    Checking if a file exists
#                   Also checks if the file exists with other extensions
#   PARAMETERS:     File            -  Input file
#   RETURNS:        valid_status    -  If the file exist, it returns true
#                                      If the file does not exist, it returns
#                                       false
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

# FUNCTION      :   check_write
# DESCRIPTION   :   This function checks if the content in the file were
#                   properly written the first time
# PARAMETERS    :   file_buffer   -   Content in the file, each line separated accordingly
#                   file          -   File being verified
# RETURNS       :   IOError -   If there is an issue, this exception is raised.
def check_write(file_buffer, file):
    # Write to the file first
    write_file(file, file_buffer)

    # Open the written file
    file_content = read_file(file)

    # Compare file content with file_buffer
    if file_buffer != file_content:
        raise IOError
