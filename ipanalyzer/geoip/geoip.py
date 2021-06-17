import requests


class GeoIP:

    def __init__(self):
        self.api_url = 'https://freegeoip.app/json/'

    def get(self, ip):
        """ Gets the geolocation of the IP address.
        If the ip is an empty string, returns the geolocation 
        of the computer public IP .

        Args:
            ip (str): The IP address.

        Returns:
            dict: The geoIP information.
        """
        url = f'{self.api_url}{ip}'
        return requests.get(url).json()