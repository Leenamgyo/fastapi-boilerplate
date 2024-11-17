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
    monkeypatch.setenv('MONGO_URL', 'localhost:27017')
    monkeypatch.setenv('MONGO_USER_NAME', 'root')
    monkeypatch.setenv('MONGO_USER_PASSWORD', 'rootpassword')
    monkeypatch.setenv('MONGO_DB_NAME', 'test-db')

@pytest.fixture
def settings():
    config = Config()
    return Settings(
        MONGO_URL=config("MONGO_URL", default=None),
        MONGO_USER_NAME=config("MONGO_USER_NAME", default=None),
        MONGO_USER_PASSWORD=config("MONGO_USER_PASSWORD", default=None),
        MONGO_DB_NAME=config("MONGO_DB_NAME", default=None)
    )


@pytest_asyncio.fixture(scope="session")
async def mongo_client(settings):    
    mongo_client: AsyncIOMotorClient = AsyncIOMotorClient(
        settings.get_mongo_url(), 
        uuidRepresentation="standard"
    )
    return mongo_client



@pytest_asyncio.fixture(scope="session")
async def mongo_db(mongo_client):
    db = mongo_client["test_db"]
    
    # setup 단계
    yield db

    # teardown 단계
    mongo_client.drop_database("test_db")
    mongo_client.close()
