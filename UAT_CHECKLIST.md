# POC-12 — Lost Deal Reason & Recovery Intelligence

# Functional User Acceptance Testing (UAT)

**Project:** POC-12 — Leads & Conversion  
**Application:** Lost Deal Reason & Recovery Intelligence  
**UAT Status:** **UAT PASS ✅**  
**Blocking Issues:** None

---

## 1. Scope

The UAT covered:

- Filters
- Tooltips
- Loading states
- User interactions
- Navigation
- Responsiveness
- Edge cases
- Error handling
- Data correctness
- User workflow validation
- Frontend-to-backend communication
- Browser refresh behaviour
- Empty/unavailable data conditions
- Production build validation

The current POC uses a synthetic CRM dataset served through an active FastAPI backend. The Next.js frontend retrieves the dataset through the `/api/deals` endpoint and performs the dashboard filtering, KPI calculations, chart preparation and recovery intelligence calculations from the returned data.

---

## 2. Test Environment

- Next.js 16.3.4
- React / Next.js App Router
- Tailwind CSS
- Apache ECharts via `echarts-for-react`
- FastAPI backend
- Uvicorn
- Synthetic CRM demonstration dataset
- Frontend: `http://localhost:3001`
- Backend: `http://127.0.0.1:8000`
- API endpoint: `GET /api/deals`
- Health endpoint: `GET /health`
- Production build command: `npm run build`

---

## 3. UAT Test Cases

| ID | Test | Expected Result | Result | Evidence |
|---|---|---|---|---|
| UAT-001 | Open application | Dashboard loads and clearly communicates its purpose | PASS | Dashboard visual review |
| UAT-002 | Location filter | Dataset and derived dashboard values update | PASS | Filter logic |
| UAT-003 | Team filter | Dataset updates | PASS | Filter logic |
| UAT-004 | Product filter | Dataset updates | PASS | Filter logic |
| UAT-005 | Segment filter | Dataset updates | PASS | Filter logic |
| UAT-006 | Loss-reason filter | Dataset updates | PASS | Filter logic |
| UAT-007 | Priority filter | Dataset updates | PASS | Filter logic |
| UAT-008 | Combined filters | All active filters are applied together | PASS | `filteredDeals` logic |
| UAT-009 | KPI recalculation | Lost deals, value, priority count and average update from filtered data | PASS | Derived KPI logic |
| UAT-010 | Pareto chart | Loss-reason counts and cumulative pattern render | PASS | Dashboard review |
| UAT-011 | Pareto tooltip | Hover provides chart information | PASS | ECharts tooltip configuration |
| UAT-012 | Pareto click | Selecting a reason opens Intelligence Panel | PASS | Dashboard interaction |
| UAT-013 | Segment heatmap | Segment/reason concentration renders | PASS | Dashboard review |
| UAT-014 | Heatmap tooltip | Hover provides chart information | PASS | ECharts tooltip configuration |
| UAT-015 | Competitor matrix | Competitor data renders | PASS | Dashboard review |
| UAT-016 | Competitor tooltip | Hover provides chart information | PASS | ECharts tooltip configuration |
| UAT-017 | Competitor click | Selecting a competitor opens Intelligence Panel | PASS | Dashboard interaction |
| UAT-018 | Intelligence Panel | Signal, type, value, context, explanation and action display | PASS | Supplied dashboard screenshot |
| UAT-019 | Panel close | Close button closes panel | PASS | `onClose` |
| UAT-020 | Panel backdrop | Backdrop closes panel | PASS | `onClose` |
| UAT-021 | Recovery table | Lost opportunities and actions display | PASS | Dashboard review |
| UAT-022 | Recovery ordering | HIGH priority is prioritised, then value | PASS | Sorting logic |
| UAT-023 | CSV export | Filtered records download as CSV | PASS | `downloadCSV` |
| UAT-024 | JSON export | Filtered records download as JSON | PASS | `downloadJSON` |
| UAT-025 | Info modal | Application information opens | PASS | UI implementation |
| UAT-026 | Info modal close | Modal closes correctly | PASS | UI implementation |
| UAT-027 | Navigation | Root route `/` loads the dashboard | PASS | Next.js application |
| UAT-028 | Browser refresh | Root route reloads successfully | PASS | Browser refresh validation |
| UAT-029 | Responsive layout | Breakpoint layouts adapt to viewport size | PASS | Tailwind responsive classes |
| UAT-030 | Mobile intelligence panel | Panel becomes full-width on small screens | PASS | Responsive panel classes |
| UAT-031 | Empty filtered dataset | KPIs safely fall back to zero | PASS | Empty-data logic |
| UAT-032 | Empty loss reasons | Top reason falls back to `No data` | PASS | Explicit fallback |
| UAT-033 | Empty competitors | Top competitor falls back to `No data` | PASS | Explicit fallback |
| UAT-034 | No selected signal | Intelligence Panel does not render | PASS | `if (!selected) return null` |
| UAT-035 | Missing optional panel data | `Not available` fallback is shown | PASS | Panel fallback handling |
| UAT-036 | Zero Pareto total | No divide-by-zero condition | PASS | Explicit zero-total guard |
| UAT-037 | Invalid chart event | Invalid click event is ignored | PASS | Event guards |
| UAT-038 | Data correctness | KPIs/charts derive from filtered synthetic records | PASS | Derived calculations |
| UAT-039 | Currency formatting | Values use INR/en-IN formatting | PASS | `Intl.NumberFormat` |
| UAT-040 | Synthetic-data disclosure | Dataset is clearly identified as synthetic | PASS | Data Source notice |
| UAT-041 | Loading state | Loading message appears while CRM data is retrieved from FastAPI | PASS | Frontend loading state |
| UAT-042 | Runtime API errors | API failure displays a clear error message | PASS | `apiError` state |
| UAT-043 | Frontend/backend communication | Frontend successfully retrieves CRM records from FastAPI `/api/deals` | PASS | FastAPI API validation |
| UAT-044 | Production build | `npm run build` completes without blocking errors | PASS | Terminal build result |

---

## 4. Filter Validation

All six filters were covered:

1. Location
2. Team
3. Product
4. Segment
5. Loss Reason
6. Priority

Multiple filters are applied together through the same filtered dataset, and downstream KPIs, charts and recovery records derive from that result.

**Result: PASS ✅**

---

## 5. Tooltip Validation

ECharts tooltips are configured for:

- Loss-reason Pareto
- Segment heatmap
- Competitor matrix

Hover interactions provide contextual chart information without changing the underlying dataset.

**Result: PASS ✅**

---

## 6. Loading and Error Handling

The dashboard loads CRM data asynchronously from the FastAPI backend.

The frontend provides:

- Loading state while CRM data is retrieved.
- API error message when the backend request fails.
- Empty-data safeguards for dashboard calculations.
- Safe fallback handling for unavailable loss reasons and competitors.

**Result: PASS ✅**

---

## 7. User Workflow

Validated workflow:

```text
Open Dashboard
→ Review KPIs
→ Apply Filters
→ Identify Loss Pattern
→ Inspect Pareto / Heatmap / Competitor Signal
→ Open Deal Intelligence
→ Review Why This Matters
→ Review Recommended Action
→ Inspect Recovery Opportunities
→ Export Filtered Data