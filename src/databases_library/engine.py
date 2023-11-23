__version__='1.0.2'
__author__='Ioannis Tsakmakis'
__date_created__='2023-11-22'

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
import os, json

def create_db_engine():
    local_directory = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(local_directory, 'mysql_config.json')

    with open(config_path,'r') as f:
        config = json.load(f)

engine = create_engine(url=f'{config["DBAPI"]}://{config["username"]}:{config['password']}@{config["host-ip"]}/{config["database"]}', 
                       pool_pre_ping=True)
class Base(DeclarativeBase):
    pass
