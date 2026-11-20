# FastAPI + React + PostgreSQL (Docker Compose)

Small, runnable demo with three services:

- **Frontend:** React + Vite, built to static files and served with Nginx.
- **Backend:** FastAPI + SQLAlchemy, with exactly one custom API endpoint: `GET /api/items`.
- **Database:** PostgreSQL 17 with a persistent Docker volume.

Nginx proxies `/api/` to the backend, so the browser uses the same origin. No CORS setup is needed.

## Run

Requires Docker Engine/Desktop with Docker Compose v2.

```bash
cp .env.example .env
# Optionally edit .env
docker compose up --build -d
```

Open **http://localhost:8080** (or your configured `APP_PORT`).

Try the API (through the frontend reverse proxy):

```bash
curl http://localhost:8080/api/items
# [{"id":1,"name":"First item"},{"id":2,"name":"Second item"}]
```

FastAPI auto-generated docs are at **http://localhost:8080/docs** only if you add an Nginx proxy location for `/docs` and `/openapi.json`; they are not forwarded by this deliberately minimal example.

## Useful commands

```bash
docker compose ps
docker compose logs -f backend
docker compose down
# Deletes all stored PostgreSQL data:
docker compose down -v
```

## Project layout

```text
backend/
  app/main.py         FastAPI endpoint, SQLAlchemy model, seed data
  requirements.txt
  Dockerfile
frontend/
  src/main.jsx        React view; fetches /api/items
  src/style.css
  index.html
  nginx.conf          Routes /api/ to FastAPI
  Dockerfile          Multi-stage Vite build + Nginx
compose.yaml          db, backend, frontend, postgres_data
.env.example
```

## How it works

1. PostgreSQL is started and marked healthy.
2. FastAPI creates the `items` table on startup and inserts two example records only when the table is empty.
3. The React page requests `GET /api/items`.
4. Nginx forwards the request to the FastAPI service, which reads PostgreSQL and returns JSON.

This is a **development/demo example**, not production-hardened. Change the default database password; add migrations (e.g., Alembic), proper authentication, and security controls for real deployments.
