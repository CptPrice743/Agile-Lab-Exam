import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_status(client):
    response = client.get('/status')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'

def test_sum_route(client):
    response = client.get('/sum?a=3&b=5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['results'] == 8.0

    response = client.get('/sum?a=-2.5&b=4.5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['results'] == 2.0
