import requests
import pytest


@pytest.fixture
def yogie_data():
    pass

Base_URL = 'https://ru.yougile.com/api-v2'
Key = "vtsfYq5LbIk8I4nz3fY2a4nKXMiZkloKmQcKHVtuGUB-OZqzkJeiTE2jIAp-N5Zv"


def test_auth():
    creds = {
        'login': 'sv025751@gmail.com',
        'password': '123456Sibmail',
        'name': 'Skypro'
        }
    response = requests.post(
        'https://ru.yougile.com/api-v2/auth/companies', json=creds)
    assert response.status_code == 200


def test_post():
    data = {
        "title": "ГОСУДАРСТВО",
        "users": {}
    }

    response = requests.post(Base_URL + "/projects", json=data, headers={
        "Authorization": f"Bearer {Key}"
    })

    assert response.status_code == 201


def test_put():
    data = {
        "title": "Changed name project",
        "deleted": False,
        "users": {}
    }
    projectId = "70ef67c7-8d9f-41a0-9291-f0b851d16aef"
    response = requests.put(Base_URL + f"/projects/{projectId}", json=data,
                            headers={
                                "Authorization": f"Bearer {Key}"
                            })
    print(response.url)
    assert response.status_code == 200


def test_list_get():
    data = {
        "title": "Changed name project",
        "timestamp": 1748585643280,
        "users": {},
        "id": "70ef67c7-8d9f-41a0-9291-f0b851d16aef",
        "deleted": False
    }
    projectId = "70ef67c7-8d9f-41a0-9291-f0b851d16aef"
    response = requests.get(Base_URL + f"/projects/{projectId}", json=data,
                            headers={
                                "Authorization": f"Bearer {Key}"
                            })
    assert response.status_code == 200