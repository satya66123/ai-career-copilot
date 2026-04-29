# System Design

## Requirements

### Functional
- Resume analysis
- ATS scoring
- Job recommendations
- Chat assistant

### Non-Functional
- Fast response
- Secure authentication
- Scalable architecture

---

## Design Approach

### 1. Modular Design
Each feature is isolated into agents.

### 2. Orchestrator Pattern
Central control for:
- Managing flow
- Combining results

### 3. Stateless Processing
Each request:
- Independent
- No dependency on previous calls

---

## Scaling Strategy

### Current
- Single machine
- Local LLM

### Future
- API-based LLM (OpenAI)
- Microservices
- Load balancing

---

## Trade-offs

| Decision | Trade-off |
|--------|---------|
| Local LLM | Lower cost vs slower |
| Streamlit | Fast dev vs limited UI |
| Monolith | Simplicity vs scalability |

---

## Future Enhancements
- Real-time job scraping
- Resume versioning
- AI interview simulator