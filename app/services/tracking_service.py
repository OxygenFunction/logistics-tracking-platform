from app.database import conn
from datetime import datetime

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


def create_tracking_event(event):

    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO tracking_event
        (
            shipment_id,
            event_type,
            location,
            event_time,
            description
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """,
        (
            event.shipment_id,
            event.event_type,
            event.location,
            datetime.now(),
            event.description
        )
    )
    conn.commit()
    cur.close()

    update_shipment_status(
        event.shipment_id,
        event.event_type
    )

    return {
        "message": "Tracking event created"
    }


def update_shipment_status(
    shipment_id,
    status
):

    cur = conn.cursor()
    cur.execute(
        """
        UPDATE shipment
        SET status = %s
        WHERE id = %s
        """,
        (
            status,
            shipment_id
        )
    )
    conn.commit()

    cur.close()