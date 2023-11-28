__version__='1.0.6'
__author__='Ioannis Tsakmakis'
__date_created__='2023-10-20'
__last_updated__='2023-11-28'

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import os, json
from contextlib import contextmanager

local_directory = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(local_directory, 'mysql_config.json')

with open(config_path,'r') as f:
    config = json.load(f)

engine = create_engine(url=f'{config["DBAPI"]}://{config["username"]}:{config['password']}@{config["host-ip"]}/{config["database"]}',
                         pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine)

# Define a context manager for sessions
@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = SessionLocal()
    try:
        yield session  # The session is provided to the block of code using the context manager
        session.commit()  # Commit changes if everything goes well
    except Exception as e:
        session.rollback()  # Roll back changes if an exception occurs
        raise e
    finally:
        session.close()  # Close the session at the end

class Base(DeclarativeBase):
    pass
