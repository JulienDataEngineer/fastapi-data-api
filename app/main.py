from fastapi import FastAPI, HTTPException
from app.database import get_db_connection

app = FastAPI(
    title="Data Warehouse API",
    description="API REST pour exposer les données du Data Warehouse PostgreSQL",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "API Data Warehouse opérationnelle"}

@app.get("/api/v1/clients")
def get_clients():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT client_id, nom, email, ville, tranche_age FROM dim_clients ORDER BY client_id;")
        clients = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"count": len(clients), "data": clients}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/analytics/sales-by-city")
def get_sales_by_city():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT 
                c.ville, 
                COUNT(f.vente_id) AS nb_ventes,
                SUM(f.montant_ttc) AS total_ttc
            FROM fact_ventes f
            JOIN dim_clients c ON f.client_key = c.client_key
            GROUP BY c.ville
            ORDER BY total_ttc DESC;
        """
        cursor.execute(query)
        metrics = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"data": metrics}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))