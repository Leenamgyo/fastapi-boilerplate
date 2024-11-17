from motor.motor_asyncio import AsyncIOMotorClient

from src.config import settings
from src.mongodb.manage import ping_mongo

MONGO_URL = settings.MONGO_URL
MONGO_DB_NAME = settings.MONGO_DB_NAME
# MONGO_USER_NAME = settings.MONGO_USER_NAME
# MONGO_PASSWORD = settings.MONGO_USER_PASSWORD

mongo_client: AsyncIOMotorClient = None 

async def connect():
    global mongo_client 
    mongo_client: AsyncIOMotorClient = AsyncIOMotorClient(
        settings.MONGO_URL, 
        uuidRepresentation="standard"
    )
    is_connected = await ping_mongo(mongo_client)

    if not is_connected:
        print("MongoDB 연결 실패!")
        return False
    else:
        print("MongoDB 연결 성공!")
        return True 

async def close():
    global mongo_client
    if mongo_client:
        mongo_client.close()

async def get_client() -> AsyncIOMotorClient:
    if mongo_client is None:
        await connect()
    return mongo_client

async def get_mongo_db():
    return mongo_client[MONGO_DB_NAME]

