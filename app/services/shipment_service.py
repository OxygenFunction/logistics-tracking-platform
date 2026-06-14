from app.database import conn
from app.schemas import ShipmentCreate

def get_all_shipments():

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


def get_shipment_by_id(shipment_id):

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


def create_shipment(shipment: ShipmentCreate):

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
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """,
        (
            shipment.shipment_number,
            shipment.origin,
            shipment.destination,
            "CREATED",
            shipment.shipper_id,
            shipment.carrier_id,
            shipment.container_id
        )
    )
    conn.commit()
    cur.close()

    return {
        "message": "Shipment created successfully"
    }