from pyx12 import parser, error_handler

class X12EDIParser:
    """
    A class to parse X12 EDI files into an internal JSON/XML format.
    """

    def __init__(self):
        pass

    def parse(self, x12_data):
        """
        Parses the X12 EDI data.

        :param x12_data: X12 EDI data as a string.
        :return: A dictionary containing the parsed data or errors.
        """
        errh = error_handler.ErrorHandler()
        parsed_data = parser.parse(x12_data, errh)
        
        if errh.has_errors():
            return {"status": "error", "errors": errh.get_errors()}
        else:
            return {"status": "success", "data": parsed_data}
