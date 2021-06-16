from ipanalyzer.parser import IPFinder
import os


EXAMPLES_DIR = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'examples')


def test_find_5000_ips():
    parser = IPFinder()
    file_path = os.path.join(EXAMPLES_DIR, 'list_of_ips.txt')
    assert len(parser.find(file_path)) == 5000


def test_file_with_no_ips():
    parser = IPFinder()
    file_path = os.path.join(EXAMPLES_DIR, 'no_ips.txt')
    assert len(parser.find(file_path)) == 0


def test_file_with_some_ips():
    parser = IPFinder()
    ips_in_file = [
        '33.33.53.155',
        '186.167.42.67',
        '236.220.190.72',
        '208.128.240.230',
        '123.42.170.221']
    file_path = os.path.join(EXAMPLES_DIR, 'some_ips.txt')
    result = parser.find(file_path)
    assert result.issubset(ips_in_file)
