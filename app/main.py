from fastapi import FastAPI
from app.database import conn
from app.schemas import ShipmentCreate

app = FastAPI()

#-------------------------------------------------

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


#-------------------------------------

from app.services.shipment_service import (
    get_all_shipments,
    get_shipment_by_id,
    create_shipment
)
from app.services.tracking_service import (
    get_tracking_events
)

@app.get("/shipments")
def get_shipments():
    return get_all_shipments()

@app.get("/shipments/{shipment_id}")
def get_shipment(shipment_id: int):
    return get_shipment_by_id(shipment_id)

@app.post("/shipments")
def create_new_shipment(
    shipment: ShipmentCreate
):
    return create_shipment(shipment)

#------------------------------------------------------------------

@app.get("/shipments/{shipment_id}/events")
def get_events(shipment_id: int):
    return get_tracking_events(shipment_id)