import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

load_dotenv()

URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

HEADERS = {
	'Accepts': 'application/json',
	'X-CMC_PRO_API_KEY': os.getenv('CMC_PRO_API_KEY'),
}

PARAMETERS = {
	'start': '1',
	'limit': '11',
	'convert': 'USD'
}

CSV_PATH = "/mnt/nfs/homes/lsalin/api.csv"

def api_runner():
	with requests.Session() as session:
		session.headers.update(HEADERS)

		try:
			response = session.get(URL, params=PARAMETERS)
			data = response.json()

		except (ConnectionError, Timeout, TooManyRedirects) as e:
			print(f"Error while connecting to {URL}: {e}")
			return

		df = pd.json_normalize(data['data'])
		df['timestamp'] = pd.to_datetime('now')

		if os.path.isfile(CSV_PATH):
			df.to_csv(CSV_PATH, mode='a', header=False)
		else:
			df.to_csv(CSV_PATH)

		print('API Runner successfully executed')

while True:
	start_time = time.time()
	api_runner()
	time.sleep(max(60 - (time.time() - start_time), 0))
