from ipanalyzer import GeoIP

keys = ['ip', 'country_code', 'country_name', 'region_code', 'region_name',
        'city', 'zip_code', 'time_zone', 'latitude', 'longitude', 'metro_code']


def test_geoip_keys():
    geoip = GeoIP()
    geoloc = geoip.get('')
    assert all(key in keys for key in geoloc)


def test_geoip_ip():
    geoip = GeoIP()
    geoloc = geoip.get('8.8.8.8')
    assert geoloc['ip'] == '8.8.8.8'


def test_geoip_country():
    geoip = GeoIP()
    geoloc = geoip.get('8.8.8.8')
    assert geoloc['country_code'] == 'US'


def test_geoip_region_code():
    geoip = GeoIP()
    geoloc = geoip.get('8.8.8.8')
    assert geoloc['region_code'] == 'MO'


def test_geoip_zip_code():
    geoip = GeoIP()
    geoloc = geoip.get('8.8.8.8')
    assert geoloc['zip_code'] == '63367'
