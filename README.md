# micro_form — Microservicio FastAPI de gestión de formularios

[![Python](https://img.shields.io/badge/Python-3.10+-3670A0?style=flat-square&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat-square)](https://www.sqlalchemy.org/)

Microservicio independiente para la **gestión de formularios** dentro de un sistema mayor (cuestionarios, encuestas, formularios de evaluación). FastAPI + SQLAlchemy + PostgreSQL, con Procfile para despliegue en Heroku/Railway/Render.

> Proyecto académico (USCO) — uno de los microservicios que conforman un sistema de calidad. Hermano de [`micro_ev`](https://github.com/jbeleno/micro_ev) (evaluaciones) y [`back_calidad`](https://github.com/jbeleno/back_calidad) (monorepo equivalente).

---

## Stack

| Categoría | Tecnología |
|---|---|
| Framework | FastAPI 0.115 |
| ORM | SQLAlchemy 2.0 |
| Base de datos | PostgreSQL |
| Validación | Pydantic 2.10 |
| Servidor | uvicorn |
| Despliegue | Procfile (Heroku, Railway, Render) |

## Quick start

```bash
git clone https://github.com/jbeleno/micro_form.git
cd micro_form/microservicio_formularios

cp ../.env.example .env
# Editar .env con tu DATABASE_URL

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload
# → http://localhost:8000/docs
```

## Estructura

```
micro_form/
├── microservicio_formularios/
│   ├── app/
│   │   ├── main.py        # FastAPI app + routes + CORS
│   │   ├── models.py      # SQLAlchemy ORM
│   │   ├── schemas.py     # Pydantic
│   │   ├── crud.py
│   │   └── database.py    # Lee DATABASE_URL del env
│   ├── Procfile
│   └── requirements.txt
├── .env.example
└── .gitignore
```

## Mejoras pendientes

- Migrar `@app.on_event("startup")` (deprecado) al patrón `lifespan`.
- Migraciones con Alembic en lugar de `Base.metadata.create_all()`.
- Tests con `pytest` + `httpx.AsyncClient`.
- CORS específico en producción (hoy `allow_origins=["*"]`).

---

## Licencia

Proyecto académico — Universidad Surcolombiana (USCO).
