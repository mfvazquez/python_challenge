import requests


class ApiIp:

    def __init__(self):
        self.api_url = ''

    def url_format(self, ip):
        return f'{self.api_url}{ip}'

    def get(self, ip):
        """ Returns the requests response in json format.

        Args:
            ip (str): A valid IP address.

        Returns:
            dict: The API response information.
        """
        url = self.url_format(ip)
        return requests.get(url).json()
