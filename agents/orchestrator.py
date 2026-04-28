from agents.resume_agent import optimize_resume
from agents.ats_agent import calculate_ats_score
from agents.semantic_ats_agent import semantic_ats_score
from agents.job_fit_agent import analyze_job_fit

def run_all_agents(resume, job_description, strict_mode=True):

    result = {}

    result["optimized_resume"] = optimize_resume(
        resume, job_description, strict_mode
    )

    result["keyword_ats"] = calculate_ats_score(
        resume, job_description
    )

    result["semantic_ats"] = semantic_ats_score(
        resume, job_description
    )

    result["job_fit"] = analyze_job_fit(
        resume, job_description, strict_mode
    )

    return result