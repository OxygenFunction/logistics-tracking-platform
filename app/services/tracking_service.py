from app.database import conn
from datetime import datetime

VALID_TRANSITIONS = {
    "CREATED": ["LOADED"],
    "LOADED": ["DEPARTED"],
    "DEPARTED": ["ARRIVED"],
    "ARRIVED": ["CUSTOMS_CLEARED"],
    "CUSTOMS_CLEARED": ["DELIVERED"],
    "DELIVERED": []
}

def validate_transition(
    current_status,
    next_status
):

    allowed_statuses = VALID_TRANSITIONS.get(
        current_status,
        []
    )

    return next_status in allowed_statuses


def get_shipment_status(shipment_id):

    cur = conn.cursor()
    cur.execute(
        """
        SELECT status
        FROM shipment
        WHERE id = %s
        """,
        (shipment_id,)
    )
    row = cur.fetchone()
    cur.close()

    return row[0]


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

    current_status = get_shipment_status(
        event.shipment_id
    )
    if not validate_transition(
        current_status,
        event.event_type
    ):
        return {
            "error":
            f"Invalid transition: "
            f"{current_status} -> "
            f"{event.event_type}"
    }
    
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