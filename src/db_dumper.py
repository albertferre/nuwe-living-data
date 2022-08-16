from pymongo import MongoClient


def dump(json_data: dict, db_name: str='nuwe', collection_name: str='coinmarketcap'):
    client = MongoClient()

    dblist = client.list_database_names()
    if "my_database" in dblist:
        print("The database exists.")
    mydb = client[db_name]
    mycol = mydb[collection_name]

    #insert a document to the collection
    x = mycol.insert_one(json_data)
    print(x)


if __name__ == "__main__":
    json_data = { "name": "Saranya", "address": "Kochi" }
    dump(json_data)