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
    row_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return row_id


def update_result(row_id, optimized_resume, ats_score):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE resumes
    SET optimized_resume = %s, ats_score = %s
    WHERE id = %s
    """

    cursor.execute(query, (optimized_resume, ats_score, row_id))
    conn.commit()

    cursor.close()
    conn.close()