import abc
# This file defines a strategy pattern
class Strategy:
    @abc.abstractmethod
    def encrypt_text(self, input_text):
        pass
    @abc.abstractmethod
    def decrypt_text(self,cipher_text):
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
                    cipher_text += 'TT'
                # Apply encryption scheme
                else:
                    # Taking the ASCII code for the input character and subtracting a value of 16 from it
                    cipher_char = ascii_plain_text - 16
                    # If the resulting outChar value is less than 32, another step must be taken:
                    if cipher_char < 32:
                        cipher_char = (cipher_char - 32) + 144
                    # Transforming result to 2 digit hexadecimal value
                    cipher_text += format(cipher_char, 'X')

        return cipher_text

    def decrypt_text(self, cipher_text):
        plain_text = ""
        # Transversing the string using range
        n = 2
        for index in range(0, len(cipher_text), n):
            # The carriage return characters are not decrypted.
            if "\n" in cipher_text[index]:
                plain_text += cipher_text[index]
            else:
                char_pair = cipher_text[index: index + n]
                # If the pair of characters is the sequence TT
                # Tt simply transforms into a <tab> character (ASCII value 9) in the output file.
                if char_pair == 'TT':
                    plain_text += '\t'
                else:
                    # Converting from hex to decimal and adding 16
                    plain_char = int(char_pair, 16)
                    plain_char += 16
                    # If the resulting outChar value is greater than 127, then another step is taken
                    if plain_char > 127:
                        plain_char = (plain_char - 144) + 32
                    # Transforming result to a char
                    plain_text += chr(plain_char)
        return plain_text
