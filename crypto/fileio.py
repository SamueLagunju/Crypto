# PROJECT       :   Crypto
# FILE          :   fileio.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-07
# DESCRIPTION   :   The functions in this file are used to

import os
from PIL import Image

available_extensions = [".txt", ".pdf", ".jpeg"]


def file_deconstruct(valid_files):
    file_stems = []
    file_extensions = []
    file_names = []
    
    for valid_file in valid_files:
        file_stem, file_extension = os.path.splitext(valid_file)
        file_stems.append(file_stem)
        file_extensions.append(file_extension)
        file_names.append(valid_file)
        
    return (file_stems, file_extensions, file_names)


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
def read_binary_file(input_file):
    with open(input_file, "rb") as file_pointer:
        file_buffer = file_pointer.read()
        # for cnt, line in enumerate(file_pointer):
        #     file_buffer += line
    return file_buffer


# FUNCTION      :   read_text_file
# DESCRIPTION   :   This function reads an existing file and extract its content
# PARAMETERS    :   input_file  -   Input file used for reading
# RETURNS       :   file_buffer -   Content in the file, each line separated accordingly
def read_text_file(input_file):
    file_buffer = ""
    with open(input_file, "r") as file_pointer:
        for cnt, line in enumerate(file_pointer):
            file_buffer += line
    return file_buffer


# FUNCTION      :   write_text_file
# DESCRIPTION   :   This function writes content to an existing text file
# PARAMETERS    :   output_file -   Output file used for writing
#                   content     -   Content in the file, each line separated accordingly
# RETURNS       :   N/A
def write_text_file(output_file, content):
    with open(output_file, "w") as file_pointer:
        file_pointer.write(content)


# FUNCTION      :   write_binary_file
# DESCRIPTION   :   This function writes content to an existing binary file
# PARAMETERS    :   output_file -   Output file used for writing
#                   content     -   Content in the file, each line separated accordingly
# RETURNS       :   N/A
def write_binary_file(output_file, content):
    with open(output_file, "wb") as file_pointer:
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


# FUNCTION      :   read_image
# DESCRIPTION   :   This function reads an existing image and extract its content
# PARAMETERS    :   input_file  -   Input file used for reading
# RETURNS       :   image_buffer -   Content in the image, an image object
def read_image(input_file):
    image_buffer = Image.open(input_file)
    return image_buffer


# FUNCTION      :   write_text_file
# DESCRIPTION   :   This function writes content to an existing text file
# PARAMETERS    :   output_file -   Output file used for writing
#                   content     -   Content in the file, each line separated accordingly
# RETURNS       :   N/A
def write_image(output_file, content):
    size = (400, 300)
    outImg = Image.frombytes('RGBA', size, content, 'raw')
    outImg.save(output_file)
