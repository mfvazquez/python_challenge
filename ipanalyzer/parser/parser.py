import re


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
            line = file.readline()
            while line:
                ips.update(self.pattern.findall(line))
                line = file.readline()
        return ips
