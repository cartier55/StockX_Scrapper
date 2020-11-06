import requests
from urllib.parse import urlencode
import pprint as p

API_URL = 'https://stockx.com/api/products/509c6166-53d4-49bf-9221-fc10cb298911/activity?'


PAYLOAD = {
    "state": "480",
    "currency": "USD",
    "limit": 203,
    "page": "1",
    "sort": "createdAt",
	"order": "DESC",
	"country": "US"
}

HEADERS = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'referer': 'https://stockx.com/supreme-patchwork-mohair-cardigan-multicolor',
}

response = requests.get(f'{API_URL}' + urlencode(PAYLOAD), headers=HEADERS).json()


ProductActivity = response['ProductActivity']
amount = [i['amount'] for i in ProductActivity]
tprofit = list()
with open('text.txt', 'w+') as f:
	for price in amount:
		profit = price - 188
		tprofit.append(profit)
		print(f'Sale Price:Profit--------------{price}:{profit}')
		f.write(f'Sale Price:Profit--------------{price}:{profit}\n')
print('-'*40)
ave = sum(tprofit)/len(amount)
print(f'Raw Sale Average--------------{ave}')
with open('text.txt', 'a') as f:
	f.write('-'*40+'\n')
	f.write(f'Raw Sale Average--------------{ave}')
