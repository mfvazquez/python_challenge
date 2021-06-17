from .api import ApiIp


class GeoIP(ApiIp):

    def __init__(self):
        self.api_url = 'https://freegeoip.app/json/'
        self.api_name = 'geoip'
