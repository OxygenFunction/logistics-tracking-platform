import time
import psycopg2


def get_connection():

    for i in range(10):
        try:
            conn = psycopg2.connect(
                host="db",
                database="logistics_db",
                user="postgres",
                password="postgres"
            )
            return conn

        except Exception as e:
            print(f"DB not ready, retry {i+1}/10")
            time.sleep(2)

    raise Exception("Could not connect to DB")

conn = get_connection()