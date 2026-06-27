import psycopg2
import pytest


@pytest.fixture
def db_cursor():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="qa_db",
        user="qa_user",
        password="qa_pass",
    )
    cur = conn.cursor()

    yield cur

    conn.rollback()
    cur.close()
    conn.close()


def test_insert_and_check_data(db_cursor):
    db_cursor.execute(
        "INSERT INTO test_cases (title, status) VALUES (%s, %s);",
        ("E2E Test", "Passed"),
    )
    db_cursor.execute("SELECT * FROM test_cases WHERE status = 'Passed'")
    result = db_cursor.fetchone()

    assert result is not None, "Резултать пустой"
    assert result[2] == "Passed", "Статус не равен Passed"
