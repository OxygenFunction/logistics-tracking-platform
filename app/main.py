from fastapi import FastAPI
from fastapi import Body
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

@app.get("/shipments/{shipment_id}")
def get_shipment(shipment_id: int):

    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM shipment
        WHERE id = %s
        """,
        (shipment_id,)
    )

    row = cur.fetchone()

    cur.close()

    return row

@app.get("/shipments/{shipment_id}/events")
def get_tracking_events(shipment_id: int):

    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            event_type,
            location,
            event_time
        FROM tracking_event
        WHERE shipment_id = %s
        ORDER BY event_time
        """,
        (shipment_id,)
    )

    rows = cur.fetchall()

    cur.close()

    return rows

@app.post("/shipments")
def create_shipment(data: dict = Body(...)):

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO shipment
        (
            shipment_number,
            origin,
            destination,
            status,
            shipper_id,
            carrier_id,
            container_id
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s
        )
        """,
        (
            data["shipment_number"],
            data["origin"],
            data["destination"],
            "CREATED",
            data["shipper_id"],
            data["carrier_id"],
            data["container_id"]
        )
    )

    conn.commit()

    cur.close()

    return {
        "message": "shipment created"
    }