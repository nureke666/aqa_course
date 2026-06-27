import psycopg2
from psycopg2.extras import RealDictCursor


class DBClient:
    def __init__(self, host, port, dbname, user, password):
        self.conn = psycopg2.connect(
            host=host, port=port, dbname=dbname, user=user, password=password
        )

    def insert_test_case(self, title: str, status: str):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO test_cases (title, status) VALUES (%s, %s);",
                (title, status),
            )

    def get_test_case_by_title(self, title):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM test_cases WHERE title = %s", (title,))
            return cur.fetchone()

    def close_connection(self):
        self.conn.rollback()
        self.conn.close()
