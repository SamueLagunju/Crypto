class Crypter:
    def __init__(self, input_file, strategy):
        self.input_file = input_file
        self.strategy = strategy

    def print_input_file(self):
        print(self.input_file)

    def encrypt_txt(self, plain_text):
        return self.strategy.encrypt_text(plain_text)

    def decrypt_txt(self, cipher_text):
        return self.strategy.decrypt_text(cipher_text)
