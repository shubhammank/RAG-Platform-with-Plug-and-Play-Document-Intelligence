from fastapi.testclient import TestClient
from api.server import app

client=TestClient(app)

def test_health():
    r=client.get('/health')
    assert r.status_code==200
