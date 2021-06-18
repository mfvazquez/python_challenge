# IP analyzer

## Installation

### Prerequisites

To run the application Python 3 and the following package is needed:

```
requests
```

### Installing from source

Run the following commands:

```bash
git clone https://github.com/mfvazquez/python_challenge.git
cd python_challenge
pip install -r requirements.txt
```

## Usage example

### From the command line

Run the following command with two arguments:

```bashrdap
python ipanalyzer.py input.txt output.json
```

Where:

* `input.txt` is the input text file with IP addresses in it.
* `output.json` is the output file with the Geo IP and RDAP lookups for each IP address.

For example:

```bash
python ipanalyzer.py list_of_ips.txt output.json
```

The file `output.json` has the following structure:

```
{
  [IP]: 
  {
    "GeoIP": [geo_ip_data],
    "RDAP": [RDAP_data]
  },
  ...
}
```

The file content can be converted to a dictionary with the function `json.load`, as shown in the following example:

```python
import json
  
# Opening JSON file
with open('output.json') as json_file:
    data = json.load(json_file)
```

### ipanalyzer

Import the module `ipanalyzer` in your python code and use the function `ip_analysis` to process a file with IP addresses.
See the script [ipanalyzer](https://github.com/mfvazquez/python_challenge/blob/readme/ipanalyzer.py) as example.

### IpFinder

To find IP addresses from a python script use an `IpFinder` object
in your python code.

```python
from ipanalyzer import IpFinder


ipfinder = IpFinder()
ips = ipfinder.find('list_of_ips.txt')
```

### GeoIP

To make a Geo IP lookup in your python code use a `GeoIP` object.

```python
from ipanalyzer import GeoIP


geoip = GeoIP()
geo_data = geoip.get('8.8.8.8')
```

### Rdap

Similar to `GeoIP`, just create an `Rdap` object to make a RDAP lookup.

```python
from ipanalyzer import Rdap


rdap = Rdap()
rdap_data = rdap.get('8.8.8.8')
```

## Tests

### Prerequisites

To run the tests the following package is needed:

```
pytest
```

### Installing from source

Install the requirements to run the tests, for this project run the following command:

```bash
pip install -r test_requirements.txt
```

### Running the tests

Just run the following command in the root directory:

```
pytest
```

For more information about running tests with pytest please visit its official [documentation](https://docs.pytest.org/en/6.2.x/contents.html).

## Improvements

* Add an option to clear the cache. Otherwise it will increase its size over time.
* Add an option to filter IP addresses.
* Imeplement a frontend for the application.
* Create a new class in charge of the read/write in the cache dir.
