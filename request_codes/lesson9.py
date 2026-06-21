import requests
import pytest
from jsonschema import validate

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["id", "name", "email"]
}

def test_user_schema():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()

    validate(instance=data, schema=user_schema)
