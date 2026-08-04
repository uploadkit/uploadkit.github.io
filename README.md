# UploadKit docs site

Public documentation site for [UploadKit](https://uploadkit.github.io/) — modular, framework-independent upload pipelines for Python.

## Structure

- `/` — marketing landing
- `/docs/` — getting started and guides (sidebar + Pagefind search)
- `/docs/core/`, `/docs/django/`, `/docs/fastapi/`, `/docs/aiohttp/`, `/docs/flask/`
- `/docs/patterns/` — shared policy, validators, errors, JSON shape
- `/docs/security/` — `uploadkit-security` + libmagic

Hand-authored static HTML/CSS/JS. Nested tabs (pip/uv/poetry, sync/async) stay as tabs; framework guides are real URLs.

## Local preview

Serve the repo root over HTTP (absolute `/styles.css` paths need a server):

```bash
python3 -m http.server 8080
```

Regenerate docs pages after content edits (shared sidebar chrome):

```bash
python3 _generate_docs.py
```

Rebuild the search index:

```bash
npx pagefind@1.3.0 --site . --output-subdir pagefind
```

## Deploy

GitHub Actions (`.github/workflows/pages.yml`) indexes with Pagefind and deploys via GitHub Pages.

In the repo **Settings → Pages**, set source to **GitHub Actions** (not “Deploy from a branch”) so the workflow can publish.

## Package status

### uploadkit (core)

[![CI](https://github.com/uploadkit/uploadkit/actions/workflows/ci.yml/badge.svg)](https://github.com/uploadkit/uploadkit/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/uploadkit/uploadkit/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://github.com/uploadkit/uploadkit/blob/main/pyproject.toml)

### uploadkit-django

[![CI](https://github.com/uploadkit/uploadkit-django/actions/workflows/ci.yml/badge.svg)](https://github.com/uploadkit/uploadkit-django/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/uploadkit/uploadkit-django/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://github.com/uploadkit/uploadkit-django/blob/main/pyproject.toml)
[![Django](https://img.shields.io/badge/django-4.2%2B-green)](https://github.com/uploadkit/uploadkit-django/blob/main/pyproject.toml)

### uploadkit-fastapi

[![CI](https://github.com/uploadkit/uploadkit-fastapi/actions/workflows/ci.yml/badge.svg)](https://github.com/uploadkit/uploadkit-fastapi/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/uploadkit/uploadkit-fastapi/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://github.com/uploadkit/uploadkit-fastapi/blob/main/pyproject.toml)
[![FastAPI](https://img.shields.io/badge/fastapi-0.110%2B-teal)](https://github.com/uploadkit/uploadkit-fastapi/blob/main/pyproject.toml)

## Links

- Site: https://uploadkit.github.io/
- Docs: https://uploadkit.github.io/docs/
- Organization: https://github.com/uploadkit
