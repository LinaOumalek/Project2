import psycopg2
from fastapi import HTTPException, status
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

load_dotenv()

def execute_query(query, values= (), fetch = False):
    conn = None
    try:
        conn = psycopg2.connect(dbname = os.getenv("DB_NAME"), user = os.getenv("DB_USER"), password = os.getenv("DB_PASSWORD"))
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(query, values)

        if fetch:
            res = cur.fetchall()
        else:
            res = None
        
        conn.commit()
        cur.close()
        conn.close()

        return res
        
    except psycopg2.IntegrityError as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
