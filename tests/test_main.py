import pytest

from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from src.main import app

client = TestClient(app)


@pytest.mark.anyio
async def test_async_read_items():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/")
        assert response.status_code == 200
