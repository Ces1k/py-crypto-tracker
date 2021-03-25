import json
import logging
from pathlib import Path
from typing import Dict, Text, Union

import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from src.coins.base import Coin
from src.lib.config import Config

MODULE_LOGGER = logging.getLogger(Path(__file__).name)


def get_current_price(config: Config, coin: Coin):
    """ """
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": config.api_key,
    }
    params = {"id": coin.id}
    response = send_request(url=config.cryptocurrency_quotes_latest_url, headers=headers, params=params)
    if response:
        data = json.loads(response)["data"]
        price = data[coin.id]["quote"]["USD"]["price"]
        return price
    else:
        return None


def send_request(
    url: Text,
    headers: Union[None, Dict] = None,
    params: Union[None, Dict] = None,
):
    with requests.Session() as session:
        if headers:
            MODULE_LOGGER.debug(f"headers: {headers}")
            session.headers.update(headers)
        if params:
            MODULE_LOGGER.debug(f"params: {params}")
            session.params.update(params)

        try:
            MODULE_LOGGER.debug(f"Sending a request to: {url}")
            response = session.get(url)
            return response.text
        except (ConnectionError, Timeout, TooManyRedirects):
            MODULE_LOGGER.error("An error has occurred during request send.", exc_info=True)
            return None
