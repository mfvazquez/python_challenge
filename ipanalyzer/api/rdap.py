from .api import ApiIp


class Rdap(ApiIp):

    def __init__(self):
        self.api_url = 'https://rdap.arin.net/registry/ip/'
        self.api_name ='rdap'