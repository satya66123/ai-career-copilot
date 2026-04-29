from database.db import get_connection

def save_resume(username,resume, job_description, model):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO resumes (username,content, job_description,model)
    VALUES (%s,%s, %s, %s)
    """

    cursor.execute(query, (username,resume, job_description,model))
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

def get_user_history(username):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT 
            id,
            content,
            job_description,
            optimized_resume,
            ats_score,
            created_at,
            model
        FROM resumes
        WHERE username = %s
        ORDER BY created_at DESC
        """

        cursor.execute(query, (username,))
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    except Exception as e:
        print("❌ get_user_history ERROR:", e)
        return []

def get_user_stats(username):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*), AVG(ats_score) FROM resumes WHERE username=%s",
            (username,)
        )

        count, avg = cursor.fetchone()

        cursor.close()
        conn.close()

        return {"total": count or 0, "avg_score": int(avg or 0)}