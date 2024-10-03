import logging
from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# basic configuration
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# configuring SQLAlchemy logger
alchemy = logging.getLogger('SQLAlchemy')
alchemy_handler = logging.FileHandler(f'{os.getenv('logging_path')}/SQLAlchemy.log')
alchemy_handler.setLevel(logging.INFO)
alchemy_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
alchemy.addHandler(alchemy_handler)
alchemy.propagate = False

# configuring influxdb logger
influx = logging.getLogger('influxdb')
influx_handler = logging.FileHandler(f'{os.getenv('logging_path')}/influx.log')
influx_handler.setLevel(logging.INFO)
influx_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
influx.addHandler(influx_handler)
influx.propagate = False

# configuring aws utils logger
aws_utils = logging.getLogger('aws_utils')
aws_utils_handler = logging.FileHandler(f'{os.getenv('logging_path')}/aws_utils.log')
aws_utils_handler.setLevel(logging.INFO)
aws_utils_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
aws_utils.addHandler(aws_utils_handler)
aws_utils.propagate = False

# configuring data retriever logger
data_retriever = logging.getLogger('data_retriever')
data_retriever_handler = logging.FileHandler(f'{os.getenv('logging_path')}/data_retriever.log')
data_retriever_handler.setLevel(logging.INFO)
data_retriever_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
data_retriever.addHandler(data_retriever_handler)
data_retriever.propagate = False