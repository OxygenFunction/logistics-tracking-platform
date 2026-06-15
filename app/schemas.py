from pydantic import BaseModel
from app.database import conn

class ShipmentCreate(BaseModel):
    shipment_number: str
    origin: str
    destination: str
    shipper_id: int
    carrier_id: int
    container_id: int

class TrackingEventCreate(BaseModel):
    shipment_id: int
    event_type: str
    location: str
    description: str