# 🚀 AI Career Copilot

An end-to-end **AI-powered career assistant** that helps users optimize resumes, improve ATS scores, identify skill gaps, and receive personalized job recommendations using a **multi-agent architecture with local LLMs**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?logo=streamlit)
![MySQL](https://img.shields.io/badge/Database-MySQL-blue?logo=mysql)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green)
![Architecture](https://img.shields.io/badge/Architecture-Multi--Agent-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)
---

## 🌟 Features

### 📄 Resume Optimization
- Tailors resumes based on job descriptions
- Improves structure, keywords, and clarity

### 📊 ATS Scoring
- Keyword-based scoring
- Semantic similarity scoring
- Missing keyword detection

### 🧠 Job Fit Analysis
- Evaluates how well a candidate matches a role
- Provides actionable feedback

### 🎯 Job Recommendations
- Suggests suitable roles based on resume
- Explains why the candidate fits

### 📊 Resume Breakdown
- Skills match
- Experience match
- AI readiness score

### 🧠 Skill Roadmap
- Identifies missing skills
- Provides step-by-step learning path

### 🔍 Keyword Generator
- Generates ATS-friendly keywords for any role
- Categorized into skills, technologies, tools

### 💬 AI Chat Assistant
- Resume-aware career guidance
- Interview preparation
- Resume improvement suggestions

### 📊 User Analytics
- Total analyses
- Average ATS score

### 📄 PDF Export
- Download optimized resume in PDF format

### 🗂️ History Tracking
- Stores past resumes
- Displays ATS scores and timestamps

---

## 🧠 System Architecture

```

User → Streamlit UI → Orchestrator → Agents → Ollama (LLM) → Response

````

### 🔹 Components

- **Frontend**: Streamlit (interactive UI)
- **Backend**: Python services
- **AI Layer**: Ollama (local LLM)
- **Database**: MySQL
- **Architecture**: Multi-Agent + Orchestrator Pattern

---

## ⚙️ Tech Stack

- **Language**: Python
- **Frontend**: Streamlit
- **Backend**: Flask-style modular services
- **Database**: MySQL
- **AI/LLM**: Ollama (Mistral, LLaMA3, Phi3)
- **Libraries**:
  - requests
  - reportlab
  - streamlit

---

## 🧩 Multi-Agent Design

Each feature is handled by a specialized agent:

- Resume Agent
- ATS Agent
- Semantic Agent
- Job Fit Agent
- Job Recommendation Agent
- Scoring Agent
- Roadmap Agent
- Keyword Agent

All agents are coordinated by a central **Orchestrator**.

---

## 🔄 Workflow

1. User inputs resume + job description
2. Data stored in MySQL
3. Orchestrator triggers agents
4. Agents process using LLM
5. Results aggregated and returned
6. UI displays structured insights

---

## 🚀 Installation

### 1. Clone Repo

```bash
git clone https://github.com/satya66123/ai-career-copilot.git
cd ai-career-copilot
````

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup MySQL

Create database:

```sql
CREATE DATABASE career_copilot;
```

Update DB config in:

```
database/db_config.py
```

---

### 5. Run Ollama

```bash
ollama serve
ollama run mistral
```

---

### 6. Run App

```bash
streamlit run app.py
```

---

## 📸 Screenshots (Add Later)

* Resume Analyzer
* ATS Dashboard
* Chat Assistant
* Job Recommendations

---

## 🔐 Security Features

* Input validation
* Rate limiting
* Session management
* Secure authentication

---

## ⚖️ Design Decisions

| Decision           | Reason                    |
| ------------------ | ------------------------- |
| Local LLM (Ollama) | Privacy + cost efficiency |
| Multi-Agent System | Modularity + scalability  |
| Streamlit          | Rapid UI development      |
| MySQL              | Persistent storage        |

---

## 🚧 Future Enhancements

* Real job scraping (LinkedIn/Indeed)
* Resume version comparison
* AI interview simulator
* SaaS deployment
* Model performance comparison

---

## 💼 How to Describe This Project

> Built a multi-agent AI career platform with resume optimization, ATS scoring (keyword + semantic), job recommendations, skill roadmap generation, and context-aware chat using local LLMs.

---

### ✅ Completed (v1.0)
- Resume Optimization
- ATS Scoring (Keyword + Semantic)
- Job Fit Analysis
- Job Recommendations
- Skill Roadmap
- Keyword Generator
- AI Chat Assistant (Context-aware)
- Multi-Agent Architecture
- User Authentication + History
- PDF Export
- Analytics Dashboard

---

### 🔜 Phase 2 (Next Enhancements)
- [ ] Resume Keyword Coverage % (matched vs missing)
- [ ] Auto-inject keywords into resume
- [ ] Resume version comparison
- [ ] Save & reload past optimized resumes
- [ ] Better UI (tabs, charts, progress bars)

---

### 🔜 Phase 3 (Advanced Intelligence)
- [ ] Real job scraping (LinkedIn / Indeed APIs)
- [ ] Job matching score (multi-JD ranking)
- [ ] AI interview simulator
- [ ] Resume ranking vs other candidates (mock benchmarking)
- [ ] Personalized career path prediction

---

### 🔜 Phase 4 (Production Ready)
- [ ] Deploy on cloud (Streamlit Cloud / Render)
- [ ] Replace local LLM with API fallback (OpenAI / Groq)
- [ ] Caching & performance optimization
- [ ] Logging & monitoring
- [ ] CI/CD pipeline

---

### 🔜 Phase 5 (SaaS Version)
- [ ] User dashboard with analytics charts
- [ ] Subscription model (Freemium / Pro)
- [ ] Resume templates marketplace
- [ ] Team / recruiter dashboard
- [ ] Multi-language support

---

## 👨‍💻 Author

**Satya**

* GitHub: [https://github.com/satya66123](https://github.com/satya66123)
* LinkedIn: [https://www.linkedin.com/in/satya-srinath-nekkanti-08b012a3](https://www.linkedin.com/in/satya-srinath-nekkanti-08b012a3)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

---

<!--suppress HtmlDeprecatedAttribute -->
---

<p align="center">
  <img src="https://img.shields.io/badge/v1.0-Completed-success?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-Completed-success?style=for-the-badge&logo=github" />
</p>

<p align="center">
  <b>🚀 AI Career Copilot — Production Ready</b>
</p>




