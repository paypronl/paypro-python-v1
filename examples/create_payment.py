from __future__ import print_function

import paypro

client = paypro.Client('API_KEY')
client.setCommand('create_payment')
client.setParams({
  'consumer_email': 'test@paypro.nl',
  'amount': 1500,
  'return_url': 'https://www.test.nl/thank-you',
  'pay_method': 'ideal/ABNANL2A'
})

response = client.execute()