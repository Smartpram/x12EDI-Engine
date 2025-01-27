class EDITransformer:
    """
    A class to expose parsing and transformation capabilities via a user-friendly interface.
    """

    def __init__(self):
        self.parser = X12EDIParser()
        self.transformer = TransformationEngine()

    def process(self, x12_data):
        """
        Processes the X12 EDI data.

        :param x12_data: X12 EDI data as a string.
        :return: A dictionary containing the transformation result or errors.
        """
        parsed_data = self.parser.parse(x12_data)
        if parsed_data["status"] == "success":
            xml_output = self.transformer.transform_to_xml(parsed_data["data"])
            return {"status": "success", "xml_output": xml_output}
        else:
            return {"status": "error", "errors": parsed_data["errors"]}
