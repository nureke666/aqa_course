from pydantic_settings import BaseSettings, SettingsConfigDict

class TestConfig(BaseSettings):
    base_url: str
    admin_password: str
    max_retries: int

    model_config = SettingsConfigDict(env_file=".env")

config = TestConfig()

print(config.base_url)
print(config.max_retries)