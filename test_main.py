# test_main.py - Tests unitaires FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_my_test():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json()['message'] == 'HELLO WORLD'

def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'