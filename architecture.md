# System Architecture

## High-Level Architecture

User → Streamlit UI → Orchestrator → Agents → Ollama LLM → Response

## Components

### 1. Frontend
- Streamlit UI
- Sidebar controls
- Chat interface

### 2. Backend
- Python services
- Business logic
- Validation layer

### 3. AI Layer
- Ollama (Local LLM)
- Prompt engineering
- Response generation

### 4. Multi-Agent System
- Resume Agent
- ATS Agent
- Semantic Agent
- Job Recommendation Agent
- Roadmap Agent

### 5. Orchestrator
- Central controller
- Combines outputs from all agents

### 6. Database
- MySQL
- Stores:
  - Users
  - Resumes
  - Scores
  - History

## Flow

1. User inputs resume + job description
2. Data saved in DB
3. Orchestrator calls agents
4. Agents process using LLM
5. Results combined and returned
6. UI displays structured output