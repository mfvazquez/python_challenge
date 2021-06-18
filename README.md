# IP analyzer

## Installation

### Prerequisites

To run the application Python 3 and the following package is needed:

```
requests
```

### Installing from source

Run the following commands:

```
git clone https://github.com/mfvazquez/python_challenge.git
cd python_challenge
pip install -r requirements.txt
```

## Usage example

### From the command line

Run the following command with two arguments:

```
python ipanalyzer.py input.txt output.json
```

Where:

* `input.txt` is the input text file with IP addresses in it.
* `output.json` is the output file with the Geo IP and RDAP lookups for each IP address.

For example:

```
python ipanalyzer.py list_of_ips.txt output.json
```

## Tests

### Prerequisites

To run the tests the following package is needed:

```
pytest
```

### Installing from source

Install the requirements to run the tests, for this project run the following command:

```
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