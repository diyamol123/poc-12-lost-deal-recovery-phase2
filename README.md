# PoC 12 — Lost Deal Reason & Recovery Intelligence

A decision-support dashboard for analysing lost CRM deals, identifying recurring loss reasons and competitive signals, and surfacing recovery-oriented actions.

## Overview

This PoC transforms lost-deal records into an interactive intelligence dashboard.

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

### Responsive Design

The dashboard was tested across:

- Desktop
- Tablet
- Mobile

---

## Technology Stack

- Next.js
- React
- TypeScript
- Tailwind CSS
- Apache ECharts
- ECharts React integration

---

## Project Structure

```text
poc-12-lost-deal-recovery/
│
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
├── public/
│
├── VAR_REPORT.md
├── UAT_CHECKLIST.md
├── README.md
├── package.json
├── package-lock.json
└── ...
## Live Deployment

https://poc-12-lost-deal-recovery.vercel.app/