from database.db import get_connection

def save_resume(resume, job_description):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO resumes (content, job_description)
    VALUES (%s, %s)
    """

    cursor.execute(query, (resume, job_description))
    conn.commit()

    cursor.close()
    conn.close()