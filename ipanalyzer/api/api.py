import requests
import os
import json
import tempfile

CACHE_DIR = os.path.join(tempfile.gettempdir(), 'ipanalyzer-cache')


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
            return self._cache_lookup(ip)
        except FileNotFoundError:
            output = requests.get(self.url_format(ip)).json()
            self._cache_store(ip, output)
            return output

    def _cache_lookup(self, ip):
        """Searchs for `ip` data in the cache directory.
        If the file exists, return its content. Otherwise
        raise `FileNotFoundError`.

        Args:
            ip (str): The IP address.

        Returns:
            [dict]: A dictionary with the last request in cache.
        """
        with open(os.path.join(CACHE_DIR, f'{self.api_name}_{ip}')) as cache_file:
            return json.load(cache_file)

    def _cache_store(self, ip, data):
        """Stores the `ip` data in cache.

        Args:
            ip (str): The IP address.
            data (dict): Data to store in a json file.
        """

        if not os.path.isdir(CACHE_DIR):
            os.mkdir(CACHE_DIR)

        with open(os.path.join(CACHE_DIR, f'{self.api_name}_{ip}'), 'w') as cache_file:
            json.dump(data, cache_file)
