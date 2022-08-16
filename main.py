"""This is the main module of the project."""
import os
import logging

from dotenv import load_dotenv

from src.api_data import coinmarket_api_data
from src.db_dumper import dump

DEFAULT_LOGGING_PATTERN = (
    "%(asctime)s - %(name)s - %(levelname)s"
    " - %(filename)s > %(funcName)s:%(lineno)d - %(message)s"
    )
logging.basicConfig(format=DEFAULT_LOGGING_PATTERN, level=logging.INFO)

os.chdir(os.path.dirname(__file__))

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("api_key")

    data = coinmarket_api_data(api_key)

    dump(data, "db", 27017)
