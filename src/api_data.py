import requests
import json
import logging
import pickle

log = logging.getLogger(__name__)

def coinmarket_api_data(api_key:str) -> dict:

    log.info('Fetching data from Coinmarketcap API')
    headers = {'X-CMC_PRO_API_KEY': api_key}
    response = requests.get(
        'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC',
        headers=headers
        )
    if response.status_code != 200:
        raise Exception('Error fetching data from Coinmarketcap API')
    else:
        log.info("Data fetched from Coinmarketcap API successfully")
        data = json.loads(response.text)

    return data

#if __name__ == '__main__':
    #print(coinmarket_api_data('6db7fc06-6935-4797-8bc5-8cfa2d80ad1f'))
