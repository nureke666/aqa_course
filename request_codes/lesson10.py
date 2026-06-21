import pytest
import requests
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    username: str
    email: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    gender: str
    image: str | None = None

def test_login_and_get_profile():
    URL = "https://dummyjson.com/auth/login"
    payload = {
        "username": "emilys",
        "password": "emilyspass",
    }
    response = requests.post(URL, data=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    token = data["accessToken"]

    URL_2 = "https://dummyjson.com/auth/me"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(URL_2, headers=headers)
    assert response.status_code == 200
    data2 = response.json()
    print(data)
    user = User.model_validate(data2)
    assert data2["username"] == "emilys"
    assert data2["lastName"] == "Johnson"


test_login_and_get_profile()