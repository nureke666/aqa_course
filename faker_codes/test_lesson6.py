import pytest
from faker import Faker
from faker.providers import BaseProvider

faker = Faker()


class SensorProvider(BaseProvider):
    def sensor_id(self) -> str:
        sensor_type = ("TEMP", "HUMIDITY", "MOTION")
        return f"SENSOR-{self.random_element(sensor_type)}-{self.random_int(min=1000, max=9999)}"


faker.add_provider(SensorProvider)


@pytest.fixture
def get_sensor_id() -> str:
    return faker.sensor_id()


def test_custom_provider(get_sensor_id):
    print(get_sensor_id)
    assert get_sensor_id.startswith("SENSOR-")
    assert get_sensor_id.count("-") == 2
