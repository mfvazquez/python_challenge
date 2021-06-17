from ipanalyzer import GeoIP

keys = ['ip', 'country_code', 'country_name', 'region_code', 'region_name',
        'city', 'zip_code', 'time_zone', 'latitude', 'longitude', 'metro_code']

IP = '8.8.8.8'


def test_geoip_keys():
    geoip = GeoIP()
    geoloc = geoip.get(IP)
    assert all(key in keys for key in geoloc)


def test_geoip_ip():
    geoip = GeoIP()
    geoloc = geoip.get(IP)
    assert geoloc['ip'] == IP


def test_geoip_country():
    geoip = GeoIP()
    geoloc = geoip.get(IP)
    assert geoloc['country_code'] == 'US'


def test_geoip_region_code():
    geoip = GeoIP()
    geoloc = geoip.get(IP)
    assert geoloc['region_code'] == 'MO'


def test_geoip_zip_code():
    geoip = GeoIP()
    geoloc = geoip.get(IP)
    assert geoloc['zip_code'] == '63367'
