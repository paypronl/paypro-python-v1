from __future__ import print_function

import paypro

client = paypro.Client('API_KEY')
client.setCommand('get_all_pay_methods')

response = client.execute()