# Web Framework Extensions

A small collection of lightweight **Web Framework Plugins / Extensions** for rapid prototyping and production-ready integration.
This project provides simple, well-documented extension patterns for **Flask** and **FastAPI** that you can drop into your projects.

**Why this repo?**
- Teachable examples of extension architecture.
- Ready-to-use middleware, routers, and app factories.
- Sponsor-friendly: small, focused, and extendable — perfect for GitHub Sponsors.

## Features

- `web_exts.flask_ext.FlaskExt` — a Flask extension providing:
  - `init_app(app)` registration
  - a status blueprint (`/ext/status`)
  - request middleware that adds `g.ext_start_time`
- `web_exts.fastapi_ext.FastAPIExt` — a FastAPI extension providing:
  - `get_router()` returns an APIRouter with `/ext/status`
  - a dependency `get_request_id` that injects request IDs
  - ASGI middleware to log request duration

## Quickstart

1. Create virtualenv and install:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run Flask example:
```bash
python examples/flask_app.py
# Open http://127.0.0.1:5000/ext/status
```

3. Run FastAPI example:
```bash
uvicorn examples.fastapi_app:app --reload
# Open http://127.0.0.1:8000/ext/status
```

## Sponsorship

If you find this useful, please consider sponsoring to support:
- more integrations (Django, Starlette, Sanic)
- extended middleware and observability features
- maintenance and security updates

Add a `FUNDING.yml` file and Sponsor button on the repo for an easy support flow.

## Structure

- `src/web_exts` — extension implementations
- `examples` — runnable example apps
- `docs` — usage and design notes
- `tests` — small unit tests

## License

MIT
