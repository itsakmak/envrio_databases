__version__='1.0.4'
__author__='Ioannis Tsakmakis'
__date_created__='2023-11-24'

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.exc import OperationalError
import os, json

local_directory = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(local_directory, 'mysql_config.json')

with open(config_path,'r') as f:
    config = json.load(f)

engine = create_engine(url=f'{config["DBAPI"]}://{config["username"]}:{config['password']}@{config["host-ip"]}/{config["database"]}',
                         pool_pre_ping=True)

def db_engine(engine,config):
    try:
        connection_check = engine.connect()
        if connection_check:
            return engine
        else:
            return create_engine(url=f'{config["DBAPI"]}://{config["username"]}:{config['password']}@{config["host-ip"]}/{config["database"]}',
                         pool_pre_ping=True)
    except OperationalError as e:
        return {'code':'Database connection issue','message':e}
class Base(DeclarativeBase):
    pass
