import requests

class IntegrationLayer:
    """
    A class to send transformed XML data to backend systems securely using HTTPS.
    """

    def __init__(self, api_endpoint, api_key):
        """
        Initializes the Integration Layer.

        :param api_endpoint: API endpoint for the backend system.
        :param api_key: API key for authentication.
        """
        self.api_endpoint = api_endpoint
        self.api_key = api_key

    def send_data(self, xml_data):
        """
        Sends XML data to the backend system.

        :param xml_data: XML data as a string.
        :return: HTTP status code of the request.
        """
        headers = {
            "Content-Type": "application/xml",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(self.api_endpoint, data=xml_data, headers=headers)
        return response.status_code
