import re
import os
import json
import tempfile
import hashlib

CACHE_DIR = os.path.join(tempfile.gettempdir(), 'ipanalyzer-cache')
CACHE_FILE = os.path.join(CACHE_DIR, 'parser')


class IpFinder:

    def __init__(self):
        self.pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    def find(self, filename):
        """ Returns a set of IP addresses found in the given file.

        Args:
            filename (str): The file name to search for IP addresses.

        Returns:
            set: A set of IP addresses.
        """
        ips = set()
        with open(filename) as file:
            content = file.read()

        try:
            ips = self._cache_lookup(content)
        except FileNotFoundError:
            ips = set()

        if not ips:
            ips.update(self.pattern.findall(content))
            self._cache_store(content, ips)

        return ips

    def __digest(self, content):
        """Returns the md5 content digest.

        Args:
            content (str): The file content.

        Returns:
            str: The md5 digest.
        """
        md5_hash = hashlib.md5()
        md5_hash.update(content.encode("utf-8"))
        return md5_hash.hexdigest()

    def _cache_lookup(self, content):
        """Looks if the latest file processed has the same 
        md5 message digest. If it is the same, returns the
        data in cache, otherwise returns an empty set.

        Args:
            content (str): The file content.

        Returns:
            [set]: A set with the data stored in cache.
        """

        with open(CACHE_FILE) as cache_file:
            cache = json.load(cache_file)

        if cache['md5'] == self.__digest(content):
            print("old data found")
            return set(cache['data'])
        return set()

    def _cache_store(self, content, data):
        """Stores the data in cache.

        Args:
            content (str): The file content.
            data (set): The data to be stored in cache.
        """

        if not os.path.isdir(CACHE_DIR):
            os.mkdir(CACHE_DIR)

        cache_data = {'data': list(data), 'md5': self.__digest(content)}

        with open(CACHE_FILE, 'w') as cache_file:
            json.dump(cache_data, cache_file)
