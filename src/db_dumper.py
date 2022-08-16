"""This module contains the functions to dump data into a MongoDB database."""
import logging
from pymongo import MongoClient

log = logging.getLogger(__name__)


def dump(
    json_data: dict, host: str, port: int, db_name: str = "nuwe", collection_name: str = "coinmarketcap"
):
    """This function dumps the data into a MongoDB database.

    :param json_data: The data to be dumped.
    :type json_data: dict
    :param host: The host of the MongoDB database.
    :type host: str
    :param port: The port of the MongoDB database.
    :type port: int
    :param db_name: ds name, defaults to "nuwe"
    :type db_name: str, optional
    :param collection_name: collection name, defaults to "coinmarketcap"
    :type collection_name: str, optional
    """
    log.info("Connecting to MongoDB")
    client = MongoClient(host, port)

    mydb = client[db_name]
    mycol = mydb[collection_name]

    log.info("inserting data into MongoDB")
    mycol.insert_one(json_data)
    log.info("Finished inserting data into MongoDB")
