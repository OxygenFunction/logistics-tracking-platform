INSERT INTO shipper (
    name,
    email,
    phone
)
VALUES
(
    'Apple',
    'apple@test.com',
    '123456'
),
(
    'Tesla',
    'tesla@test.com',
    '888888'
);

INSERT INTO carrier (
    name,
    contact_email
)
VALUES
(
    'Maersk',
    'contact@maersk.com'
),
(
    'COSCO',
    'contact@cosco.com'
);

INSERT INTO container (
    container_number,
    container_type
)
VALUES
(
    'MSKU1234567',
    '40FT'
),
(
    'MSKU7654321',
    '20FT'
);

INSERT INTO shipment (
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
    'SHP001',
    'Shanghai',
    'Los Angeles',
    'CREATED',
    1,
    1,
    1
),
(
    'SHP002',
    'Shenzhen',
    'Hamburg',
    'CREATED',
    1,
    1,
    1
);

INSERT INTO tracking_event (
    shipment_id,
    event_type,
    location,
    event_time,
    description
)
VALUES
(
    1,
    'CREATED',
    'Shanghai',
    NOW(),
    'Shipment created'
),
(
    1,
    'LOADED',
    'Shanghai Port',
    NOW(),
    'Container loaded onto vessel'
);