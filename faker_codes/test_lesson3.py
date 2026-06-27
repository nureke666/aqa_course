import pytest
from faker import Faker


@pytest.fixture
def generate_product():
    faker = Faker()
    return {
        "name": faker.word(),
        "price": faker.random_int(min=100, max=9999),
        "barcode": faker.ean13(),
    }


def test_product_validation(generate_product):
    assert generate_product["price"] > 0
    assert len(generate_product["barcode"]) == 13
