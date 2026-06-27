import requests
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, field_validator


class Setting(BaseSettings):
    base_url: str

    model_config = SettingsConfigDict(env_file=".env")


config = Setting()


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str | None = None

    @field_validator("email")
    @classmethod
    def check_email_correct(cls, value):
        if "@" not in value:
            raise ValueError("Not correct email")
        return value


class SupportData(BaseModel):
    url: str
    text: str


class UserResponse(BaseModel):
    data: UserData
    support: SupportData


def test_request():
    response = requests.get(config.base_url)
    data = response.json()
    user_obj = UserResponse.model_validate(data)
    print(user_obj.data.first_name)
    print(user_obj.support.url)
