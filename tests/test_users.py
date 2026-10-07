import json
from framework.api.client import APIClient
from config.config import BASE_URL

def test_create_user():
    client = APIClient(BASE_URL)

    with open("test_data/users.json", "r") as file:
        data = json.load(file)

    response = client.post("/users", data)

    assert response.status_code == 201
def test_get_user():
    client = APIClient(BASE_URL)
    response = client.get("/users/1")
    assert response.status_code == 200

def test_update_user():
    client = APIClient(BASE_URL)

    data = {
        "name": "Shirley Updated",
        "email": "updated@example.com"
    }

    response = client.put("/users/1", data)

    assert response.status_code == 200

    result = response.json()

    assert result["id"] == 1
    assert result["name"] == "Shirley Updated"
    assert result["email"] == "updated@example.com"

def test_delete_user():
    client = APIClient(BASE_URL)

    response = client.delete("/users/1")

    assert response.status_code == 200

def test_get_nonexistent_user():
    client = APIClient(BASE_URL)

    response = client.get("/users/99999")

    assert response.status_code == 404