""" This module contains the methods to fetch data from the CoinMarketCap API. """

import json
import logging
import requests

log = logging.getLogger(__name__)


def coinmarket_api_data(api_key: str) -> dict:
    """This method calls the CoinMarketCap API and returns the data.

    :param api_key: The coinMarketCap API key.
    :type api_key: str
    :raises Exception: If the API key is not valid.
    :return: The data from the CoinMarketCap API.
    :rtype: dict
    """

    log.info("Fetching data from Coinmarketcap API")
    headers = {"X-CMC_PRO_API_KEY": api_key}
    response = requests.get(
        "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC",
        headers=headers,
    )
    if response.status_code != 200:
        raise Exception("Error fetching data from Coinmarketcap API")

    log.info("Data fetched from Coinmarketcap API successfully")
    data = json.loads(response.text)

    return data


# if __name__ == '__main__':
# print(coinmarket_api_data('6db7fc06-6935-4797-8bc5-8cfa2d80ad1f'))
