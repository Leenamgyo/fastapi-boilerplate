import pytest
import pytest_asyncio
from src.mongodb.manage import ping_mongo


@pytest.mark.asyncio
async def test_ping_mongo(mongo_client):
    is_connected = await ping_mongo(mongo_client)
    assert is_connected is True, "MongoDB ping failed"

# 테스트 함수 예시
@pytest.mark.asyncio
async def test_insert_and_find(mongo_db):
    collection = await mongo_db["test_collection"]
    collection.insert_one({"name": "Alice"})
    result = collection.find_one({"name": "Alice"})
    assert result["name"] == "Alice"
    
    # # 데이터 조회
    # found_data = await collection.find_one({"name": "test_user"})
    # assert found_data["name"] == "test_user"
    # assert found_data["age"] == 30

    # # 테스트 데이터 삭제
    # await collection.delete_one({"name": "test_user"})
    

    