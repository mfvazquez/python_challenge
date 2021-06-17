import requests
import os
import json


CACHE_DIR = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '.cache')


class ApiIp:

    def __init__(self):
        self.api_url = ''
        self.api_name = 'api'

    def url_format(self, ip):
        return f'{self.api_url}{ip}'

    def get(self, ip):
        """ Returns the requests response in json format.

        Args:
            ip (str): A valid IP address.

        Returns:
            dict: The API response information.
        """
        try:
            return self.__cache_lookup(ip)
        except FileNotFoundError:
            output = requests.get(self.url_format(ip)).json()
            self.__cache_store(ip, output)
            return output

    def __cache_lookup(self, ip):
        with open(os.path.join(CACHE_DIR, f'{self.api_name}_{ip}')) as cache_file:
            return json.load(cache_file)

    def __cache_store(self, ip, data):

        if not os.path.isdir(CACHE_DIR):
            os.mkdir(CACHE_DIR)

        with open(os.path.join(CACHE_DIR, f'{self.api_name}_{ip}'), 'w') as cache_file:
            json.dump(data, cache_file)
