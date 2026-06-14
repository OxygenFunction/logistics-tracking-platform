from app.database import conn

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