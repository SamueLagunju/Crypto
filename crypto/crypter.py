# PROJECT       :   Crypto
# FILE          :   crypter.py
# PROGRAMMER    :   Samuel Lagunju
# DATE          :   2020-08-19
# DESCRIPTION   :   This file contains the class Crypter.


#   NAME          :   Crypter
#   PURPOSE       :   The Crypter class has been created to
#                     accurately extends the behavior of a Strategy pattern
#                     It is an interface of interest for encrypting/decrypting
class Crypter:

    # METHOD        :   init
    # DESCRIPTION   :   This function is called after the instance has been created
    # PARAMETERS    :   input_file  -   File meant for encrypting/decrypting
    #                   strategy    -   Algorithm use to work on the input file
    # RETURNS       :   N/A
    def __init__(self, input_file, strategy):
        self.input_file = input_file
        self.strategy = strategy

    # METHOD        :   print_input_file
    # DESCRIPTION   :   This function is used to print the entire content of the input file.
    # PARAMETERS    :   N/A
    # RETURNS       :   Prints output of file.
    def print_input_file(self):
        print(self.input_file)

    # METHOD        :   encrypt_txt
    # DESCRIPTION   :   This function is a default strategy behavior
    # PARAMETERS    :   plain_text  -   Text that is about to be encrypted into cipher text
    # RETURNS       :   encrypted text
    def encrypt_txt(self, plain_text):
        return self.strategy.encrypt_text(plain_text)

    # METHOD        :   decrypt_txt
    # DESCRIPTION   :   This function is a default strategy behavior
    # PARAMETERS    :   cipher_text  -   Text that is about to be decrypted into plain text
    # RETURNS       :   decrypted text
    def decrypt_txt(self, cipher_text):
        return self.strategy.decrypt_text(cipher_text)

    def convert_ext(self, file_name, old_ext):
        return self.strategy.convert_ext(file_name, old_ext)
