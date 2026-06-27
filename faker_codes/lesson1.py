from faker import Faker

faker = Faker()

user_profile = {
    "name": faker.name(),
    "age": faker.random_int(min=0, max=100),
    "about_me": faker.sentence(),
}

print(user_profile)
