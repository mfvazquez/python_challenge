from ipanalyzer import Rdap


def test_rdap_entity():
    rdap = Rdap()
    assert rdap.get('8.8.8.8')['entities'][0]['handle'] == 'GOGL'
