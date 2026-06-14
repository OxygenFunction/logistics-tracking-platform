CREATE TABLE shipper (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(50)
);

CREATE TABLE carrier (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(255)
);

CREATE TABLE container (
    id SERIAL PRIMARY KEY,
    container_number VARCHAR(50) UNIQUE NOT NULL,
    container_type VARCHAR(50)
);

CREATE TABLE shipment (
    id SERIAL PRIMARY KEY,
    shipment_number VARCHAR(50) UNIQUE NOT NULL,
    origin VARCHAR(100),
    destination VARCHAR(100),
    status VARCHAR(50),
    shipper_id INTEGER REFERENCES shipper(id),
    carrier_id INTEGER REFERENCES carrier(id),
    container_id INTEGER REFERENCES container(id)
);

CREATE TABLE tracking_event (
    id SERIAL PRIMARY KEY,
    shipment_id INTEGER NOT NULL REFERENCES shipment(id),
    event_type VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    event_time TIMESTAMP NOT NULL,
    description TEXT
);

CREATE INDEX idx_tracking_event_shipment
ON tracking_event(shipment_id);