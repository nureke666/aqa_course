from pydantic import BaseModel

user_payload = {
    "id": 101,
    "personal_info": {"first_name": "Anna", "last_name": "Smith"},
    "devices": [
        {"device_name": "iPhone 13", "os": "iOS"},
        {"device_name": "Samsung TV", "os": "Tizen"},
    ],
}


class Device(BaseModel):
    device_name: str
    os: str


class PersonalInfo(BaseModel):
    first_name: str
    last_name: str


class User(BaseModel):
    id: int
    personal_info: PersonalInfo
    devices: list[Device]


user = User.model_validate(user_payload)
print(user.personal_info.last_name)
print(user.devices[1].device_name)
