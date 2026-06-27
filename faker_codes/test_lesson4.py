import pytest
from faker import Faker

faker = Faker()
role = ("admin", "manager", "customer")


@pytest.fixture
def generate_users():
    users_list = []

    for i in range(5):
        user = {
            "email": faker.unique.email(),
            "role": faker.random_element(role),
        }
        users_list.append(user)

    return users_list


def test_user_uniqueness(generate_users):
    print(generate_users)
    assert len(generate_users) == 5

    all_emails = []
    for i in generate_users:
        all_emails.append(i["email"])

    assert len(set(all_emails)) == 5
