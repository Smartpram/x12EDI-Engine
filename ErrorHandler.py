import logging

class ErrorHandler:
    """
    A class to handle errors and log them.
    """

    def __init__(self):
        logging.basicConfig(filename="edi_errors.log", level=logging.ERROR)

    def log_error(self, error_message):
        """
        Logs an error message.

        :param error_message: Error message to log.
        """
        logging.error(error_message)
