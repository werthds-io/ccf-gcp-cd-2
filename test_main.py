import pytest
from main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get("/")
    assert response.data == b'Hello World...again'


def test_echo(client):
    name = 'Wonderous'
    response = client.get(f"/echo/{name}")
    assert response.json == {"name-name": name}
