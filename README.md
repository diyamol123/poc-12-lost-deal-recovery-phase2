# PoC 12 — Lost Deal Reason & Recovery Intelligence

A decision-support dashboard for analysing lost CRM deals, identifying recurring loss reasons and competitive signals, and surfacing recovery-oriented actions.

## Overview

This PoC transforms lost-deal CRM records into an interactive intelligence dashboard.

Users can:

- Analyse lost deals by location, team, product, segment, loss reason, and priority
- Monitor key recovery and loss indicators
- Explore loss reasons using analytical charts
- Analyse customer-segment patterns
- Review competitive loss signals
- Open an Intelligence Panel for contextual interpretation
- Review deal-level recovery information
- Export dashboard data as CSV and JSON

> **Data note:** This PoC uses a synthetic CRM loss/follow-up dataset for demonstration and decision-support purposes. Company names and records are synthetic.

---

## Phase 2 — Containerization

Phase 2 extends the Lost Deal Recovery intelligence dashboard with a containerized application architecture.

The application includes:

- Next.js frontend
- FastAPI backend
- Docker containerization
- Docker Compose orchestration
- Frontend-to-backend API communication
- Separate frontend and backend services
- Container service networking
- Next.js API proxy configuration

The application can be built and run locally as a multi-container system using Docker Compose.

---

## Key Features

### Dashboard Intelligence

- KPI summary
- Interactive filtering
- Loss-reason analysis
- Segment analysis
- Competitive analysis
- Intelligence Panel
- Recovery recommendations
- Deal-level recovery table

### User Interactions

- Filter combinations
- Interactive chart tooltips
- Chart selection
- Intelligence Panel
- Information interface
- CSV export
- JSON export

### Backend Intelligence API

The FastAPI backend provides the API layer for the dashboard.

Available endpoints include:

- `GET /`
- `GET /health`
- `GET /api/deals`

The frontend accesses the backend through the Next.js API proxy.

### Containerization

Phase 2 includes:

- Frontend Dockerfile
- Backend Dockerfile
- Docker Compose configuration
- Docker ignore configuration
- Container service networking
- API proxy configuration

### Responsive Design

The dashboard is designed for:

- Desktop
- Tablet
- Mobile

---

## Technology Stack

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS
- Apache ECharts
- ECharts React integration

### Backend

- Python
- FastAPI
- Uvicorn

### Containerization

- Docker
- Docker Compose

---

## Project Structure

```text
poc-12-lost-deal-recovery/

├── app/
│   ├── components/
│   │   ├── DashboardCharts.tsx
│   │   ├── DecisionPanel.tsx
│   │   ├── IntelligencePanel.tsx
│   │   └── RecoveryTable.tsx
│   ├── globals.css
│   ├── layout.tsx
│   └── page.tsx
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── public/
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── package.json
├── package-lock.json
├── next.config.ts
├── vercel.json
└── README.md