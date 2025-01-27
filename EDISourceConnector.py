import os
import paramiko  # For SFTP
from cryptography.fernet import Fernet  # For encryption

class EDISourceConnector:
    """
    A class to read X12 EDI files from various sources (local, FTP, SFTP, etc.).
    Supports encryption for secure file handling.
    """

    def __init__(self, source_type, source_config, encryption_key=None):
        """
        Initializes the EDI Source Connector.

        :param source_type: Type of source (e.g., "local", "sftp").
        :param source_config: Configuration for the source (e.g., file path, FTP credentials).
        :param encryption_key: Encryption key for decrypting files (optional).
        """
        self.source_type = source_type
        self.source_config = source_config
        self.encryption_key = encryption_key

    def read_file(self, file_path):
        """
        Reads and decrypts (if necessary) the X12 EDI file.

        :param file_path: Path to the file.
        :return: Decrypted file content as a string.
        """
        if self.source_type == "local":
            with open(file_path, 'rb') as file:
                data = file.read()
                if self.encryption_key:
                    data = self._decrypt_data(data)
                return data.decode('utf-8')
        elif self.source_type == "sftp":
            # SFTP implementation
            transport = paramiko.Transport((self.source_config["host"], self.source_config["port"]))
            transport.connect(username=self.source_config["username"], password=self.source_config["password"])
            sftp = paramiko.SFTPClient.from_transport(transport)
            with sftp.open(file_path, 'rb') as file:
                data = file.read()
                if self.encryption_key:
                    data = self._decrypt_data(data)
                return data.decode('utf-8')
        else:
            raise ValueError("Unsupported source type")

    def _decrypt_data(self, data):
        """
        Decrypts data using the provided encryption key.

        :param data: Encrypted data.
        :return: Decrypted data.
        """
        fernet = Fernet(self.encryption_key)
        return fernet.decrypt(data)
