# Interview Questions & Answers

## Q1: Why did you build this project?
To solve real-world resume rejection issues using AI and automation.

## Q2: What is your system architecture?
A multi-agent AI system with:
- Orchestrator
- Independent agents
- Local LLM (Ollama)
- Streamlit frontend

## Q3: Why multi-agent design?
Separation of concerns:
- Each agent handles a specific task
- Improves scalability and maintainability

## Q4: How does ATS scoring work?
- Keyword matching
- Semantic similarity
- Missing keyword detection

## Q5: How do you handle scalability?
- Modular agents
- Stateless API calls
- Can migrate to microservices

## Q6: Why use local LLM?
- Privacy
- Cost efficiency
- Offline capability

## Q7: How do you prevent hallucination?
- Strict prompts
- Validation layers
- Controlled outputs

## Q8: What improvements would you add?
- Real job scraping
- Model comparison
- SaaS deployment