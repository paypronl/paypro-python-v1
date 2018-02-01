import os.path
from unittest import mock, TestCase

from paypro.client import Client
from paypro.error import ApiConnectionError, InvalidResponseError
from requests.exceptions import RequestException

def mockResponse(content, side_effect=None):
    mock_response = mock.Mock()
    mock_response.json.return_value = content
    if side_effect is not None:
        mock_response.json.side_effect = side_effect
    return mock_response

class TestClient(TestCase):

    def setUp(self):
        self.client = Client('API_KEY')

    @mock.patch('paypro.client.requests.post')
    def testExecute(self, mock_post):
        # Valid request
        mock_response = mockResponse(content={'data': 'test'})
        mock_post.return_value = mock_response
        self.assertEqual({'data': 'test'}, self.client.execute())

        # Invalid response
        mock_response = mockResponse(content='', side_effect=ValueError)
        mock_post.return_value = mock_response
        with self.assertRaises(InvalidResponseError):
            self.client.execute()

        # Connection errors
        mock_response = mockResponse(content={'data': 'test'}, side_effect=RequestException)
        mock_post.return_value = mock_response
        with self.assertRaises(ApiConnectionError):
            self.client.execute()

    def testSetCommand(self):
        self.client.setCommand('create_payment')
        self.assertEqual('create_payment', self.client.command)

    def testSetParam(self):
        self.client.setParam('pay_method', 'paypal/direct')
        self.assertEqual({'pay_method': 'paypal/direct'}, self.client.params)

    def testSetParams(self):
        self.client.setParams(
            {
                'pay_method': 'paypal/direct',
                'consumer_email': 'test@paypro.nl'
            }
        )
        self.assertEqual(
            {
                'pay_method': 'paypal/direct',
                'consumer_email': 'test@paypro.nl'
            },
            self.client.params
        )

    def testSetParamsAndParam(self):
        self.client.setParam('pay_method', 'paypal/direct')
        self.client.setParams(
            {
                'pay_method': 'bancontact/mistercash',
                'consumer_email': 'test@paypro.nl'
            }
        )
        self.assertEqual(
            {
                'pay_method': 'bancontact/mistercash',
                'consumer_email': 'test@paypro.nl'
            },
            self.client.params
        )

    def testGetCACert(self):
        self.assertTrue(os.path.isfile(self.client.getCACert()))