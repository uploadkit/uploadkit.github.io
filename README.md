# UploadKit docs site

Public documentation site for [UploadKit](https://uploadkit.github.io/) — modular, framework-independent upload pipelines for Python.

## Structure

- `/` — marketing landing
- `/docs/` — getting started and guides (sidebar + Pagefind search)
- `/docs/core/`, `/docs/django/`, `/docs/fastapi/`, `/docs/aiohttp/`, `/docs/odoo/`, `/docs/flask/`
- `/docs/patterns/` — shared policy, validators, errors, JSON shape
- `/docs/storage/` — boto3 / aioboto3 for AWS S3 and MinIO
- `/docs/performance/` — chunk size, S3 part size, and workers by file size
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

Static site on `main` (including committed `pagefind/` index). GitHub Pages is configured to publish from the **`main` branch root**.

Optional: `.github/workflows/pages.yml` can rebuild Pagefind and deploy via Actions (`workflow_dispatch` / push). Prefer branch publish when Actions runners are unavailable.

After content edits:

```bash
python3 _generate_docs.py
npx pagefind@1.3.0 --site . --output-subdir pagefind --glob "{index.html,docs/**/*.html}"
```

In the repo **Settings → Pages**, set source to **GitHub Actions** (not “Deploy from a branch”) so the workflow can publish.

## Package status

Coverage badges on **feature packages** (pdf / audio / office) and **cli** are
**measured** totals, not the 100% figures used by Core and framework adapters.
Gaps are mostly `metadata.py` edge cases (malformed inputs, rare security /
format branches) and CLI flag/error paths. Feature-package CI gates at 80%
where configured; cli has no coverage gate yet, so it shows CI + Python only.

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

### uploadkit-odoo

[![CI](https://github.com/uploadkit/uploadkit-odoo/actions/workflows/ci.yml/badge.svg)](https://github.com/uploadkit/uploadkit-odoo/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/uploadkit/uploadkit-odoo/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://github.com/uploadkit/uploadkit-odoo/blob/main/pyproject.toml)
[![Odoo](https://img.shields.io/badge/odoo-17%20%7C%2018-purple)](https://github.com/uploadkit/uploadkit-odoo)

### uploadkit-pdf

[![CI](https://github.com/uploadkit/uploadkit-pdf/actions/workflows/ci.yml/badge.svg)](https://github.com/uploadkit/uploadkit-pdf/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-85%25-brightgreen)](https://github.com/uploadkit/uploadkit-pdf/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://github.com/uploadkit/uploadkit-pdf/blob/main/pyproject.toml)

### uploadkit-audio

[![CI](https://github.com/uploadkit/uploadkit-audio/actions/workflows/ci.yml/badge.svg)](https://github.com/uploadkit/uploadkit-audio/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-81%25-brightgreen)](https://github.com/uploadkit/uploadkit-audio/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://github.com/uploadkit/uploadkit-audio/blob/main/pyproject.toml)

### uploadkit-office

[![CI](https://github.com/uploadkit/uploadkit-office/actions/workflows/ci.yml/badge.svg)](https://github.com/uploadkit/uploadkit-office/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-79%25-yellow)](https://github.com/uploadkit/uploadkit-office/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://github.com/uploadkit/uploadkit-office/blob/main/pyproject.toml)

### uploadkit-cli

[![CI](https://github.com/uploadkit/uploadkit-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/uploadkit/uploadkit-cli/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://github.com/uploadkit/uploadkit-cli/blob/main/pyproject.toml)

## Links

- Site: https://uploadkit.github.io/
- Docs: https://uploadkit.github.io/docs/
- Organization: https://github.com/uploadkit
