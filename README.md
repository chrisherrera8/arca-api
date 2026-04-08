# Arca API

Business Expense Tracking Platform API built with FastAPI, SQLAlchemy, and PostgreSQL.

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- [Podman](https://podman.io/) with the `podman-compose` plugin

## Setup

**1. Clone and install dependencies**

```bash
git clone <repo>
cd arca-api
uv sync --extra dev
```

**2. Configure environment**

```bash
cp .env.example .env
```

Edit `.env` and set the required values:

| Variable | Required | Notes |
|---|---|---|
| `DATABASE_URL` | Yes | Default points to `localhost:5432/arca` |
| `SECRET_KEY` | Yes | Any long random string |
| `ANTHROPIC_API_KEY` | For OCR | Receipt scanning feature |
| `RESEND_API_KEY` | For email | Approval notifications |
| `AWS_*` | For S3 storage | Only if `STORAGE_BACKEND=s3` |

**3. Start the database**

From the repo root (where `docker-compose.yml` lives):

```bash
podman-compose up -d postgres 
```

This starts PostgreSQL on `localhost:5432` with the `arca` user and database already created.

**4. Run migrations**   

```bash
uv run alembic upgrade head
```

**5. Start the server**

```bash
uv run uvicorn app.main:app --reload
```

API runs at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

## Running Tests

```bash
uv run pytest
```

## File Storage

By default, uploaded receipts are stored locally at `./uploads`. To use S3, set `STORAGE_BACKEND=s3` and fill in the `AWS_*` vars in `.env`.

## Stopping the database

```bash
podman-compose down
```

Add `-v` to also remove the persistent volume: `podman-compose down -v`


