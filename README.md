![PayPro](https://paypro.nl/images/logo-ie.png)
# Python Client for PayPro API v1
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPi Package](https://img.shields.io/pypi/v/paypro.svg)](https://pypi.python.org/pypi/paypro)
[![circleci](https://img.shields.io/circleci/project/github/RedSparr0w/node-csgo-parser.svg)](https://circleci.com/gh/paypronl/paypro-python-v1)

This library provides a Python client to connect with the PayPro API.

## Requirements
 - Python >= 3.0
 - It also depends on the Requests package
 
## Installation

Installation is done through `pip` you can use this command:

```sh
pip install paypro
```

If you want to develop or run the source you can use the supplied `Pipfile` to install all packages. To run the tests you also need to install the dev packages.

## Getting Started

Example of creating a payment:

```python
from paypro import Client

client = Client('YOUR_API_KEY')
client.setCommand('create_payment')
client.setParams(
  {
    'amount': 500,
    'consumer_email': 'test@paypro.nl',
    'pay_method': 'ideal/INGBNL2A'
  }
)
client.execute()
```

## Documentation

For guides and code examples you can go to https://paypro.nl/developers/docs.

## Tests

To run the test suite you can execute the `tests.py` file. This will run the whole suite and generates a JUnit XML file with all test results.

## Contributing

If you want to contribute to this project you can fork the repository. Create a new branch, add your feature and create a pull request. We will look at your request and determine if we want to add it.

## License
[MIT](https://github.com/paypronl/paypro-ruby-v1/blob/master/LICENSE)
