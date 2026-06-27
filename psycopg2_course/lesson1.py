import psycopg2

conn = psycopg2.connect(
    host="localhost", port="5432", dbname="qa_db", user="qa_user", password="qa_pass"
)

cur = conn.cursor()

cur.execute("SELECT version()")

db_version = cur.fetchone()
print(db_version)

cur.close()
conn.close()
