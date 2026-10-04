import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "data_warehouse",
    "user": "jul"
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
