# Logistics Tracking Platform

A backend logistics tracking service built with FastAPI and PostgreSQL.

## Features

- Shipment management
- Tracking event management
- PostgreSQL database
- RESTful APIs
- Swagger documentation

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- Git

## Run

uvicorn app.main:app --reload


logistics-tracking-platform/

│
├── app/
│   │
│   ├── main.py
│   ├── database.py
│   ├── schemas.py
│   │
│   └── services/
│       ├── shipment_service.py
│       └── tracking_service.py
│
├── database/
│   ├── schema.sql
│   └── seed.sql
│
├── requirements.txt
│
└── README.md