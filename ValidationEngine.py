class ValidationEngine:
    """
    A class to validate parsed X12 EDI data against X12 standards and trading partner rules.
    """

    def __init__(self):
        pass

    def validate(self, parsed_data):
        """
        Validates the parsed X12 EDI data.

        :param parsed_data: Parsed X12 EDI data.
        :return: A list of validation errors.
        """
        errors = []
        if not parsed_data.get("ISA"):
            errors.append("Missing ISA segment")
        return errors
