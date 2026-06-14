from fastapi import FastAPI
from app.database import conn

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Logistics Tracking Platform"
    }


@app.get("/shippers")
def get_shippers():

    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM shipper
        """
    )

    rows = cur.fetchall()

    cur.close()

    return rows

@app.get("/shipments")
def get_shipments():

    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM shipment
        """
    )

    rows = cur.fetchall()

    cur.close()

    return rows