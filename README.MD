# GridGuard AI

**Industrial Smart Grid Forecasting & Blackout Risk Intelligence Platform**  
Powered by VeraGrid + PyPSA + AI Analytics

---

## Overview

GridGuard AI is a modular, scalable smart-grid intelligence system integrating:

- **VeraGrid** – High-speed AC/DC power flow simulation
- **PyPSA** – Optimal power flow and grid optimization
- **Custom AI Engine** – LSTM / Transformer forecasting
- **Grid4C API** (optional) – External AI enhancement
- Real-time telemetry ingestion
- Infrastructure risk modeling
- Interactive drag-and-drop dashboard

### Target Users

- State Electricity Boards
- Distribution Companies (DISCOMs)
- Smart City Infrastructure Operators
- Grid Research Labs

---

## Core Capabilities

- AC/DC Power Flow Simulation
- Optimal Power Flow (OPF)
- Short Circuit & Contingency Analysis
- Time-Series Grid Simulation
- AI-Based Load Forecasting
- Blackout Risk Detection
- Transformer Stress Prediction
- Demand Response Optimization
- Real-Time Dashboard Visualization
- Model Switching (Baseline / LSTM / Transformer)
- Plugin-Based Renewable & EV Extensions

---

## Technology Stack

### Physics & Optimization Engine
- VeraGrid (AC/DC simulation, contingency analysis)
- PyPSA (OPF, capacity expansion, storage optimization)

### AI & Analytics
- PyTorch (LSTM, Transformer)
- scikit-learn (Isolation Forest)
- Grid4C API (optional augmentation)

### Backend
- Python (FastAPI)
- Celery (scheduler)
- SQLAlchemy
- Redis
- Kafka (optional high-scale mode)

### Performance-Critical Components (C/C++)
- SCADA drivers
- ONNX/TensorRT inference
- Telemetry collectors
- VeraGrid core computation

### Frontend
- React / Vanilla JS
- WebSocket streaming
- Drag-and-drop UI
- Chart.js / D3.js

### Database
- TimescaleDB (time-series optimized PostgreSQL)

---

## Installation

### Core Dependencies

```bash
pip install veragrid
pip install pypsa
pip install torch
pip install fastapi
pip install uvicorn
pip install pandas
pip install numpy
pip install scikit-learn
pip install sqlalchemy
pip install redis
```

### Optional

```bash
pip install celery
pip install kafka-python
```

---

## Project Structure

```text
gridguard-ai/
├── ingestion/
├── simulation/
├── ai/
├── risk/
├── recommendation/
├── api/
├── scheduler/
├── dashboard/
├── database/
└── config.toml
```

---

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload
```

Open API docs at `http://127.0.0.1:8000/docs`.
