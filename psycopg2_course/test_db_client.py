import pytest
from db_client import DBClient


@pytest.fixture
def db():
    client = DBClient("localhost", "5432", "qa_db", "qa_user", "qa_pass")
    yield client
    client.close_connection()


def test_db_client_methods(db):
    db.insert_test_case("Python Client Test", "Skipped")
    res = db.get_test_case_by_title("Python Client Test")

    assert res is not None
    assert res["status"] == "Skipped", "Статус не совпадает с Skipped"
