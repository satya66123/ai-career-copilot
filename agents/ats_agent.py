import re

STOPWORDS = {
    "the","and","for","with","are","you","your","job","role","company",
    "title","salary","required","preferred","responsibilities",
    "location","we","our","they","this","that","these",    "etc","using","into","based","applications","application"

}

def extract_keywords(text):
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    return list(set([w for w in words if w not in STOPWORDS]))


def calculate_ats_score(resume, job_description):
    jd_keywords = extract_keywords(job_description)
    resume_text = resume.lower()

    matched = []
    missing = []

    for word in jd_keywords:
        if word in resume_text:
            matched.append(word)
        else:
            missing.append(word)

    score = int((len(matched) / len(jd_keywords)) * 100) if jd_keywords else 0

    return {
        "score": score,
        "matched": matched[:15],
        "missing": missing[:15]
    }