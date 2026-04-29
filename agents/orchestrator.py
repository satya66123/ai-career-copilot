from agents.resume_agent import optimize_resume
from agents.ats_agent import calculate_ats_score
from agents.semantic_ats_agent import semantic_ats_score
from agents.job_fit_agent import analyze_job_fit
from agents.job_recommendation_agent import recommend_jobs
from agents.scoring_agent import resume_scoring
from agents.roadmap_agent import skill_roadmap

def run_all_agents(resume, job_description, strict_mode=True, model="mistral:latest"):

    result = {"optimized_resume": optimize_resume(
        resume, job_description, strict_mode, model
    ), "keyword_ats": calculate_ats_score(
        resume, job_description
    ), "semantic_ats": semantic_ats_score(
        resume, job_description
    ), "job_fit": analyze_job_fit(
        resume, job_description, strict_mode, model
    ), "job_recommendations": recommend_jobs(resume, model), "scoring": resume_scoring(
        resume, job_description, model
    ), "roadmap": skill_roadmap(
        resume, job_description, model
    )}

    # 🔥 NEW FEATURES

    return result