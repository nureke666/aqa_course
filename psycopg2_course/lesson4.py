import psycopg2

conn = psycopg2.connect(
    host="localhost", port="5432", dbname="qa_db", user="qa_user", password="qa_pass"
)

with conn:
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO test_cases (title, status) VALUES (%s, %s);",
            ("UI Test", "Failed"),
        )
        cur.execute("SELECT * FROM test_cases;")
        print(cur.fetchall())

conn.close()
