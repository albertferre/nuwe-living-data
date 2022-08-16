from src.api_data import coinmarket_api_data
from src.db_dumper import dump
import os
from dotenv import load_dotenv


os.chdir(os.path.dirname(__file__))


load_dotenv()
api_key = os.getenv('api_key')

data = coinmarket_api_data(api_key)

dump(data)

print('finished writing json')
