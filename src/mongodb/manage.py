

from motor.motor_asyncio import AsyncIOMotorClient

async def init_database(client: AsyncIOMotorClient, db_name: str) -> bool:
    pass 
        

async def ping_mongo(client: AsyncIOMotorClient) -> bool:
    try:
        # MongoDB에서 ping 명령어 실행
        result = await client.admin.command("ping")
        return result.get("ok", 0) == 1
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    