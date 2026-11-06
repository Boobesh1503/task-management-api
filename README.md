# Task Management REST API

A beginner-friendly backend project built with **Python, FastAPI, SQLAlchemy and SQLite**.

## Features

- Create, list, retrieve, update and delete tasks (CRUD)
- Task statuses: `pending`, `in_progress`, `completed`
- Search by task title
- Filter by status
- Pagination (`skip`, `limit`)
- Input validation and clear 404 errors
- Health-check endpoints
- Automated API tests with pytest
- Interactive Swagger documentation

## Requirements

- Python 3.10+
- pip

## Run locally (Windows PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

If PowerShell blocks activation, run this for the current terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## Run locally (macOS/Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health: http://127.0.0.1:8000/health

## API endpoints

Base path: `/api/v1`

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks` | Create a task |
| GET | `/tasks` | List tasks |
| GET | `/tasks/{task_id}` | Get one task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

### Example: create a task

```json
{
  "title": "Prepare for interview",
  "description": "Revise Python and REST API basics"
}
```

### List, search and filter

- `GET /api/v1/tasks?search=interview`
- `GET /api/v1/tasks?status=pending`
- `GET /api/v1/tasks?skip=0&limit=20`

### Update a task

```json
{
  "status": "completed"
}
```

## Run tests

```bash
pytest -q
```

Tests use the local SQLite database. For a clean test run, remove `tasks.db` before running tests.

## Project structure

```text
task-management-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       └── tasks.py
├── tests/
│   └── test_tasks.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Before production

This is a learning/demo project, not a production-hardened service. Before deploying publicly:
- Restrict CORS to trusted frontend origins.
- Add authentication and authorization.
- Use environment-managed secrets and a managed database.
- Add database migrations (Alembic), structured logging and rate limiting.
- Add CI checks and production monitoring.
- Review privacy, backup and deployment settings.

## Resume description (after you run and verify it)

Developed a Task Management REST API using Python, FastAPI, SQLAlchemy and SQLite, implementing CRUD operations, input validation, search, filtering, pagination and automated API tests with pytest.
