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
Optional
bash
Copy code
pip install celery
pip install kafka-python
Project Structure
css
Copy code
gridguard-ai/
│
├── ingestion/
│   ├── scada_driver.c
│   ├── mqtt_listener.py
│   ├── weather_client.py
│
├── simulation/
│   ├── veragrid_engine.py
│   ├── pypsa_optimizer.py
│   ├── contingency_analysis.py
│
├── ai/
│   ├── lstm_model.py
│   ├── transformer_model.py
│   ├── anomaly_detector.py
│   ├── train.py
│   ├── inference.py
│
├── risk/
│   ├── overload_model.py
│   ├── blackout_probability.py
│
├── recommendation/
│   ├── rule_engine.py
│   ├── opf_dispatch.py
│
├── api/
│   ├── main.py
│
├── scheduler/
│   ├── tasks.py
│
├── dashboard/
│   ├── src/
│   │   ├── components/
│   │   ├── plugins/
│
├── database/
│   ├── models.py
│
└── config.toml
System Architecture
java
Copy code
Smart Meters / SCADA
        ↓
SCADA Driver (C)
        ↓
MQTT / TCP
        ↓
Data Ingestion Service
        ↓
Kafka / Redis Stream
        ↓
Feature Engineering
        ↓
AI Forecast Engine
        ↓
VeraGrid Simulation
        ↓
PyPSA Optimization
        ↓
Risk Engine
        ↓
Recommendation Engine
        ↓
API Gateway
        ↓
Dashboard
Component Details
1. VeraGrid Integration (Physics Layer)
Purpose: Industrial-grade power flow simulation

Capabilities
AC Power Flow

DC Power Flow

Short Circuit Analysis

Contingency Analysis

Time-Series Simulation

Example
python
Copy code
from veragrid import Grid

grid = Grid()
grid.load_case("regional_grid_case.json")
grid.run_power_flow()
results = grid.get_bus_voltages()
Inputs
Bus data

Line impedance

Transformer capacity

Load data

Outputs
Voltage profile

Line loading %

Stability indicators

Resource Usage: CPU-intensive (optimized C backend)

2. PyPSA Integration (Optimization Layer)
Purpose: Optimal power flow & dispatch optimization

python
Copy code
import pypsa

network = pypsa.Network("grid_model.nc")
network.lopf()
Used For
Generator dispatch

Storage management

CO₂ constraints

Rolling horizon optimization

Outputs
Optimal generation schedule

Load redistribution plan

3. AI Forecast Engine
LSTM Architecture
scss
Copy code
Input → LSTM(128) → Dropout → LSTM(64) → Dense → Output
Input Schema
sql
Copy code
[Batch, Time Window, Features]
Features
Load

Temperature

Humidity

Hour encoding

Rolling mean

Stress ratio

Training
python
Copy code
optimizer = torch.optim.Adam(model.parameters())
loss = torch.nn.MSELoss()
Inference API
POST /predict

json
Copy code
{
  "predicted_load": 510,
  "confidence": 0.92
}
4. Anomaly Detection
Isolation Forest:

python
Copy code
from sklearn.ensemble import IsolationForest

model = IsolationForest()
model.fit(X)
Detects
Abnormal spikes

Transformer stress

Equipment failure patterns

5. Risk Engine
Overload Index
pgsql
Copy code
Overload Index = Predicted Load / Transformer Capacity
Weighted Risk Score
java
Copy code
Risk Score =
(Load Risk × 0.5) +
(Anomaly Score × 0.3) +
(Voltage Deviation × 0.2)
Outputs
Risk Level

Blackout Probability %

6. Recommendation Engine
Combines:

Rule-based logic

PyPSA OPF results

Example:

mathematica
Copy code
If overload > 0.9:
  → Activate backup transformer
  → Shift industrial load
  → Start demand response
UI Architecture
Features
Drag-and-Drop Components

Historical CSV Upload

Transformer Spec Upload

Weather Data Upload

Grid Topology JSON Upload

Toggles
Enable AI Forecast

Enable Anomaly Detection

Switch Model (ARIMA / LSTM / Transformer)

Enable Grid4C API Mode

Enable OPF Optimization

Panels
Load Forecast Panel

Risk Gauge

Voltage Stability Map

Transformer Stress Table

Contingency Analysis Viewer

Real-Time Updates: WebSocket streaming

Grid4C Integration (Optional)
Use Cases:

Appliance-level disaggregation

Demand-side forecasting

Fault detection

API:

bash
Copy code
POST https://api.grid4c.com/forecast
Returns enhanced demand prediction and device-level insights.

Scheduling & Optimization Internals
Scheduler (Celery Worker)
Hourly retraining

5-minute forecasting

Nightly contingency simulation

Optimization Algorithms
Linear Programming (OPF)

Rolling Horizon Optimization

Stochastic Load Modeling

Reinforcement Learning (planned)

Communication & Concurrency
Protocols
Edge → MQTT

Internal → Kafka

API → REST + WebSocket

DB → TCP (libpq)

Concurrency
Async FastAPI

Multi-threaded ingestion

Kafka offset management

Distributed locking (Redis)

Resource Profile
High Load
VeraGrid simulations

PyPSA OPF

LSTM training

Kafka cluster

Moderate
Inference

Risk engine

Low
UI

Database

Database Schema
Tables
load_data

predictions

risk_scores

anomalies

opf_results

Optimized using TimescaleDB hypertables.

Deployment
Dockerized microservices:

ingestion-service

simulation-service

ai-service

risk-service

api-gateway

dashboard

Supports
Kubernetes scaling

GPU inference nodes

Edge AI deployment

Industrial Readiness
Fault tolerance

Message replay

Blue-Green model deployment

Monitoring via Prometheus

Logging via ELK stack
