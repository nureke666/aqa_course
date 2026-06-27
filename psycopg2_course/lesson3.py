import psycopg2

conn = psycopg2.connect(
    host="localhost", port="5432", dbname="qa_db", user="qa_user", password="qa_pass"
)

cur = conn.cursor()

cur.execute(
    "UPDATE test_cases SET status=%s WHERE title=%s", ("Retest", "Payment Test")
)
cur.execute("DELETE FROM test_cases WHERE title=%s", ("Login Test",))
conn.commit()

cur.execute("SELECT * FROM test_cases")
print(cur.fetchall())

cur.close()
conn.close()
