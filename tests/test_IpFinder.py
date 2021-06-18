from ipanalyzer import IpFinder
import os
import pytest


EXAMPLES_DIR = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'examples')


def test_find_5000_ips():
    parser = IpFinder()
    file_path = os.path.join(EXAMPLES_DIR, 'list_of_ips.txt')
    assert len(parser.find(file_path)) == 5000


def test_file_with_no_ips():
    parser = IpFinder()
    file_path = os.path.join(EXAMPLES_DIR, 'no_ips.txt')
    assert len(parser.find(file_path)) == 0


def test_file_with_some_ips():
    parser = IpFinder()
    ips_in_file = [
        '33.33.53.155',
        '186.167.42.67',
        '236.220.190.72',
        '208.128.240.230',
        '123.42.170.221']
    file_path = os.path.join(EXAMPLES_DIR, 'some_ips.txt')
    result = parser.find(file_path)
    assert result.issubset(ips_in_file)


def test_cache_empty():
    parser = IpFinder()
    content = "a sample content"
    parser._cache_store(content, set())
    output_data = parser._cache_lookup(content)
    assert len(output_data) == 0

def test_cache():
    parser = IpFinder()
    content = "a sample content 1.1.1.1 with two ips 0.1.2.3"
    data = set(('1.1.1.1', '0.1.2.3'))
    parser._cache_store(content, data)
    output_data = parser._cache_lookup(content)
    assert output_data == data