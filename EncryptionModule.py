from cryptography.fernet import Fernet

class EncryptionModule:
    """
    A class to encrypt and decrypt data at rest and in transit.
    """

    def __init__(self, key):
        """
        Initializes the Encryption Module.

        :param key: Encryption key.
        """
        self.key = key

    def encrypt_data(self, data):
        """
        Encrypts data.

        :param data: Data to encrypt.
        :return: Encrypted data.
        """
        fernet = Fernet(self.key)
        return fernet.encrypt(data.encode('utf-8'))

    def decrypt_data(self, data):
        """
        Decrypts data.

        :param data: Encrypted data.
        :return: Decrypted data.
        """
        fernet = Fernet(self.key)
        return fernet.decrypt(data).decode('utf-8')
