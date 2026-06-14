import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="logistics_db",
    user="postgres",
    password="5234"
)