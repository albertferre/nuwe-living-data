"""This module contains the functions to dump data into a MongoDB database."""
import logging
from pymongo import MongoClient

log = logging.getLogger(__name__)


def dump(
    json_data: dict, db_name: str = "nuwe", collection_name: str = "coinmarketcap"
):
    """This function dumps the data into a MongoDB database.

    :param json_data: The data to be dumped.
    :type json_data: dict
    :param db_name: ds name, defaults to "nuwe"
    :type db_name: str, optional
    :param collection_name: collection name, defaults to "coinmarketcap"
    :type collection_name: str, optional
    """
    log.info("Connecting to MongoDB")
    client = MongoClient()

    dblist = client.list_database_names()
    if "my_database" in dblist:
        log.info("Database exists")
    mydb = client[db_name]
    mycol = mydb[collection_name]

    log.info("inserting data into MongoDB")
    mycol.insert_one(json_data)
