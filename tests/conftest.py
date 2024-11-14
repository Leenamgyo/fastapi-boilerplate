import sys
import os
import pytest
import pytest_asyncio

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from starlette.config import Config
from src.config import Settings

# 'src' 디렉토리를 sys.path에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

@pytest.fixture(autouse=True)
def set_env_vars(monkeypatch):
    monkeypatch.setenv('MONGO_URL', 'mongodb://localhost:27017')
    monkeypatch.setenv('MONGO_USER_NAME', 'root')
    monkeypatch.setenv('MONGO_USER_PASSWORD', 'rootpassword1133')
    monkeypatch.setenv('MONGO_DB_NAME', 'mydb')

@pytest.fixture
def settings():
    config = Config()

    return Settings(
        MONGO_URL=config("MONGO_URL", default=None),
        MONGO_USER_NAME=config("MONGO_USER_NAME", default=None),
        MONGO_USER_PASSWORD=config("MONGO_USER_PASSWORD", default=None),
        MONGO_DB_NAME=config("MONGO_DB_NAME", default=None)
    )


@pytest_asyncio.fixture()
async def mongo_client(settings):    
    MONGO_URL = settings.MONGO_URL
    MONGO_DB_NAME = settings.MONGO_DB_NAME
    MONGO_USER_NAME = settings.MONGO_USER_NAME
    MONGO_PASSWORD = settings.MONGO_USER_PASSWORD

    mongo_client: AsyncIOMotorClient = AsyncIOMotorClient(
        MONGO_URL, 
        username=MONGO_USER_NAME,
        password=MONGO_PASSWORD,
        uuidRepresentation="standard",
    )
    
    return mongo_client[MONGO_DB_NAME]
     

# @pytest.fixture    
# def mongo_client(settings):
    