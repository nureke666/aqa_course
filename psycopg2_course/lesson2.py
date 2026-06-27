import psycopg2

conn = psycopg2.connect(
    host="localhost", port="5432", dbname="qa_db", user="qa_user", password="qa_pass"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS test_cases (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100),
        status VARCHAR(20)
    );
""")

cur.execute("""
    INSERT INTO test_cases (title, status) VALUES ('Login Test', 'Passed'), ('Payment Test', 'Failed')
""")

conn.commit()

cur.execute("SELECT * FROM test_cases")
res = cur.fetchall()

for row in res:
    print(row)

cur.close()
conn.close()
