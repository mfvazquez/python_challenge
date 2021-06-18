from ipanalyzer import Rdap
import pytest

def test_rdap_entity():
    rdap = Rdap()
    assert rdap.get('8.8.8.8')['entities'][0]['handle'] == 'GOGL'

def test_rdap_cache_lookup_fails():
    rdap = Rdap()
    with pytest.raises(FileNotFoundError):
        rdap._cache_lookup('1.2.3.4')
        
        
def test_rdap_cache_store():
    rdap = Rdap()
    input_data = {'key': 'value'}
    rdap._cache_store('1.0.0.0', input_data)
    output_data = rdap._cache_lookup('1.0.0.0')
    assert input_data == output_data