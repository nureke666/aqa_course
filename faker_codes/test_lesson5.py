import pytest
import datetime
from faker import Faker

faker = Faker()


@pytest.fixture
def booking_date():
    return {
        "passenger_name": faker.name(),
        "flight_date": faker.future_date(),
        "promo_code": faker.bothify(text="SALE-####-????"),
    }


def test_booking_format(booking_date):
    assert booking_date["flight_date"] > datetime.date.today()
    assert booking_date["promo_code"].startswith("SALE-")
    print(booking_date["promo_code"])
