class TransformationEngine:
    """
    A class to transform parsed X12 EDI data into XML.
    """

    def __init__(self):
        pass

    def transform_to_xml(self, parsed_data):
        """
        Transforms parsed X12 EDI data into XML.

        :param parsed_data: Parsed X12 EDI data.
        :return: XML data as a string.
        """
        xml_data = "<root>"
        for segment in parsed_data:
            xml_data += f"<segment>{segment}</segment>"
        xml_data += "</root>"
        return xml_data
