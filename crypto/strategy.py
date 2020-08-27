import abc


# This file defines a strategy pattern
class Strategy:
    @abc.abstractmethod
    def encrypt_text(self, input_text):
        pass

    @abc.abstractmethod
    def decrypt_text(self, cipher_text):
        pass


class SeanStrategy(Strategy):
    """ Concrete strategy for Sean Clarke's encryption scheme. """

    def encrypt_text(self, plain_text):
        # DO MAGIC
        cipher_text = ""
        # Transversing the string using range function
        for pt_char_index in range(len(plain_text)):
            if "\n" in plain_text[pt_char_index]:
                cipher_text += plain_text[pt_char_index]
            else:
                # Returning plain text into integer
                ascii_plain_text = ord(plain_text[pt_char_index])
                # If the character is a <tab> (ASCII value 9) it is just TT
                if ascii_plain_text == 9:
                    cipher_text += "TT"
                # Apply encryption scheme
                else:
                    # Taking the ASCII code for the input character and subtracting a
                    # value of 16 from it
                    cipher_char = ascii_plain_text - 16
                    # If the resulting outChar value is less than 32, another step must
                    # be taken:
                    if cipher_char < 32:
                        cipher_char = (cipher_char - 32) + 144
                    # Transforming result to 2 digit hexadecimal value
                    cipher_text += format(cipher_char, "X")

        return cipher_text

    def decrypt_text(self, cipher_text):
        # plain_text = ""
        # n = 2
        # for line_index in cipher_text.readline():
        #     for index in range(0, len(cipher_text), n):
        #         char_pair = cipher_text[index: index + n]
        #         if char_pair == 'TT':
        #             plain_text += '\t'
        #         else:
        #             # Converting from hex to decimal and adding 16
        #             plain_char = int(char_pair, 16) + 16
        #
        #             if plain_char > 127:
        #                 plain_char = (plain_char - 144) + 32
        #
        #             plain_text += chr(plain_char)
        #
        # return plain_text
        plain_text = ""
        n = 2
        # Parsing the cipher text, line by line
        for cipher_line in cipher_text.splitlines():
            # Parsing each line and decrypting the file
            for index in range(0, len(cipher_line), n):
                # Capturing each pair of characters in the input line
                char_pair = cipher_line[index : index + n]
                # If the pair of characters is the sequence TT it simply transforms
                # into a <tab> character
                if char_pair == "TT":
                    plain_text += "\t"
                else:
                    # Converting from hex to decimal and adding 16
                    plain_char = int(char_pair, 16) + 16
                    # If the resulting outChar value is greater than 127, then another
                    # step is taken
                    if plain_char > 127:
                        plain_char = (plain_char - 144) + 32
                    plain_text += chr(plain_char)

            # Adding the new line character back to the line
            plain_text += "\n"
        return plain_text
