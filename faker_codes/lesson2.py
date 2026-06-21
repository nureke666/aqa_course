from faker import Faker

Faker.seed(777)
faker = Faker(locale='ru_RU')

registration_data = {
    "full_name": faker.name() + faker.last_name(),
    "username": faker.user_name(),
    "email": faker.email(),
    "password": faker.password(length=12),
}

print(registration_data)

print(faker.name())
print(faker.name())
print(faker.name())
