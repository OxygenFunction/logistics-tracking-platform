import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="logistics_db",
    user="postgres",
    password="5234"
)

cur = conn.cursor()

cur.execute("SELECT * FROM shipper")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()