# FERA 2.0

FERA (Fuel Efficiency Research & Analysis) is a research-oriented platform for studying vehicle fuel efficiency, predicting fuel consumption from vehicle telemetry, and generating explainable efficiency insights.

## Project Goals

FERA 2.0 is a professional evolution of the original FERA 1.0 prototype.

The project aims to:

- Build a reproducible data and ML pipeline
- Use real-world vehicle data where appropriate
- Separate data processing, model inference, business logic, and API concerns
- Provide explainable efficiency predictions
- Support vehicle health and anomaly analysis
- Provide an interactive frontend
- Maintain Docker as an optional deployment path

## FERA 1.0

FERA 1.0 demonstrated the original concept using:

- FastAPI
- scikit-learn
- joblib
- Synthetic fallback data
- Rule-based efficiency heuristics
- SQLite logging
- Browser frontend
- Optional Docker deployment

FERA 2.0 preserves the useful concepts while addressing the architectural and methodological limitations of the prototype.

## Current Status

The backend foundation currently includes:

- FastAPI application
- API router layer
- Application configuration
- Service layer
- Validated telemetry schemas
- Efficiency prediction contract
- Automated backend tests

The primary modelling dataset has not yet been finalized.

## Data

Datasets are maintained under `data/`.

- `data/raw/` — Original datasets
- `data/processed/` — FERA-generated datasets
- `data/external/` — Supplementary or reference datasets

Raw datasets are not committed unless their license and size permit redistribution.

## Development

Python dependencies are managed with `uv`.

Run the backend tests:

    uv run pytest

## Architecture

FERA 2.0 separates:

    Frontend
        |
        v
    API
        |
        v
    Schemas / Validation
        |
        v
    Application Services
        |
        v
    Model Boundary
        |
        v
    Data / ML Pipeline

The model implementation will be added only after the target, features, dataset limitations, and evaluation methodology have been established.

## Deployment

Docker remains supported as an optional deployment mechanism.

Local development should not require Docker.
