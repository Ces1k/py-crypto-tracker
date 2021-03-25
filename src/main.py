import argparse
import logging
from pathlib import Path
import time

from src.lib.config import Config
from src.coins import btc, eth
from src.lib.logger import setup_logger
from src.lib import bot, retriever

LOGGER_NAME = Path(__file__).name
MODULE_LOGGER = logging.getLogger(LOGGER_NAME)

COINS = {
    "btc": btc.BTC,
    "eth": eth.ETH,
}


def main():
    args = parse_arguments()
    coin = COINS[args.coin]()
    config_obj = Config()
    logger = setup_logger(name=LOGGER_NAME, config=config_obj)

    while True:
        current_price = retriever.get_current_price(config_obj, coin=coin)
        if current_price:
            message = f"Current {coin.symbol.upper()} price: {current_price}"
            logger.info(message)
        else:
            message = "Something went wrong during price retrieval! Stopping the loop..."
            logger.error(message)
            break
        bot.send_message_to_telegram(config_obj, message)
        logger.debug(f"Waiting {config_obj.request_time_interval}s for next check...")
        time.sleep(config_obj.request_time_interval)
        logger.debug("The end of waiting, restarting...")


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--coin",
        choices=["btc", "eth"],
        default="btc",
        help="Provide a name of Coin name you want to check price for",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
