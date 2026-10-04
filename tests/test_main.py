from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "API Data Warehouse opérationnelle"}

def test_get_clients():
    response = client.get("/api/v1/clients")
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_sales_by_city():
    response = client.get("/api/v1/analytics/sales-by-city")
    assert response.status_code == 200
    assert "data" in response.json()