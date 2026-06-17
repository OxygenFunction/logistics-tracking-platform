# Logistics Tracking Platform

A backend logistics tracking system inspired by modern freight-forwarding platforms such as Flexport.

## Overview

This project models real-world logistics entities and provides RESTful APIs to manage shipment lifecycles and tracking events.

Key entities include:

* Shipper
* Shipment
* Carrier
* Container
* Tracking Event

## Architecture

Shipper (1:N) Shipment (1:N) TrackingEvent

A shipment progresses through the following lifecycle:

CREATED → LOADED → DEPARTED → ARRIVED → CUSTOMS_CLEARED → DELIVERED

Status transitions are validated through a state machine to prevent invalid shipment states.

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* Docker
* Docker Compose
* Git

## Features

### Shipment Management

* Create shipments
* Retrieve shipment information
* Track shipment status

### Tracking Events

* Record shipment events
* Maintain complete event history
* Automatically update shipment status

### Database Design

* Relational schema design
* Foreign key constraints
* Indexed tracking-event queries

### Containerization

* Dockerized FastAPI service
* Dockerized PostgreSQL database
* One-command deployment via Docker Compose

## API Endpoints

GET /shipments

GET /shipments/{id}

POST /shipments

GET /shipments/{id}/events

POST /tracking-events

## Run Locally

docker compose up --build

Swagger UI:

http://localhost:8000/docs

## Project Structure

app/
├── main.py
├── schemas.py
├── database.py
└── services/
├── shipment_service.py
└── tracking_service.py

database/
├── schema.sql
└── seed.sql

Dockerfile

docker-compose.yml

requirements.txt

README.md

## Future Improvements

* Authentication and authorization
* Async database access
* Database connection pooling
* Automated CI/CD pipeline
* Monitoring and observability
