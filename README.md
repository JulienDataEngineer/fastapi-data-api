# 🚀 FastAPI Data API — Exposure Layer

API REST développée avec **FastAPI** et **Psycopg2** pour exposer les données analytiques du Data Warehouse PostgreSQL.

---

## 🛠️ Endpoints

* `GET /` : Health check de l'API.
* `GET /api/v1/clients` : Liste des clients dimensionnels.
* `GET /api/v1/analytics/sales-by-city` : Agrégation des ventes et du CA par ville.

---

## 🚀 Installation & Lancement

1. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt