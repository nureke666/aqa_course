from pydantic import BaseModel, field_validator

user_data = {"username": "qa_ninja", "email": "ninja@company.com", "age": 15}


class RegistrationData(BaseModel):
    username: str
    email: str
    age: int

    @field_validator("email")
    @classmethod
    def check_email(cls, value):
        if "@" not in value:
            raise ValueError("Not correct email")
        return value

    @field_validator("age")
    @classmethod
    def check_age(cls, value):
        if value < 17:
            raise ValueError("User must be 18 years old or more")
        return value


user = RegistrationData.model_validate(user_data)
print("Validation is successful")
