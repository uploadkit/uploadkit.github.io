#!/usr/bin/env python3
"""One-shot authoring helper: emit docs HTML pages with shared chrome."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#050510">
  <meta name="color-scheme" content="dark">
  <link rel="canonical" href="https://uploadkit.github.io{canonical}">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="UploadKit">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://uploadkit.github.io{canonical}">
  <meta property="og:image" content="https://uploadkit.github.io/uploadkit-Fav.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&amp;family=IBM+Plex+Mono:wght@400;500&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-tomorrow.min.css">
  <link href="/pagefind/pagefind-ui.css" rel="stylesheet">
  <link rel="icon" type="image/png" href="/uploadkit-Fav.png">
  <link rel="apple-touch-icon" href="/uploadkit-Fav.png">
</head>
<body class="docs-page">
  <div class="grid-bg"></div>
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="orb orb-3"></div>

  <header class="site-header">
    <a class="brand" href="/">UploadKit</a>
    <nav class="nav-links" aria-label="Primary">
      <a href="/#packages">Packages</a>
      <a href="/docs/">Docs</a>
      <a href="https://github.com/uploadkit" target="_blank" rel="noopener">GitHub</a>
    </nav>
    <button type="button" class="mobile-menu-btn" id="mobile-menu-btn" aria-label="Menu">☰</button>
  </header>

  <button type="button" class="docs-sidebar-toggle" id="docs-sidebar-toggle" aria-expanded="false" aria-controls="docs-sidebar">Menu</button>
  <div class="docs-sidebar-backdrop" id="docs-sidebar-backdrop"></div>

  <div class="docs-layout">
    <aside class="docs-sidebar" id="docs-sidebar" aria-label="Docs">
      <div class="docs-search" id="docs-search"></div>
      <div class="docs-nav-group">
        <p class="docs-nav-label">Start</p>
        <ul class="docs-nav">
          <li><a href="/docs/"{active_getting}>Getting started</a></li>
        </ul>
      </div>
      <div class="docs-nav-group">
        <p class="docs-nav-label">Reference</p>
        <ul class="docs-nav">
          <li><a href="/docs/core/"{active_core}><span class="docs-nav-link-inner"><span class="tab-icon tab-icon--python" aria-hidden="true"></span>Core</span></a></li>
          <li><a href="/docs/patterns/"{active_patterns}>Common patterns</a></li>
          <li><a href="/docs/storage/"{active_storage}>Storage</a></li>
          <li><a href="/docs/security/"{active_security}>Security</a></li>
        </ul>
      </div>
      <div class="docs-nav-group">
        <p class="docs-nav-label">Frameworks</p>
        <ul class="docs-nav">
          <li><a href="/docs/django/"{active_django}><span class="docs-nav-link-inner"><span class="tab-icon tab-icon--django" aria-hidden="true"></span>Django</span> <span class="badge badge-live">Supported</span></a></li>
          <li><a href="/docs/fastapi/"{active_fastapi}><span class="docs-nav-link-inner"><span class="tab-icon tab-icon--fastapi" aria-hidden="true"></span>FastAPI</span> <span class="badge badge-live">Supported</span></a></li>
          <li><a href="/docs/aiohttp/"{active_aiohttp}><span class="docs-nav-link-inner"><span class="tab-icon tab-icon--aiohttp" aria-hidden="true"></span>aiohttp</span> <span class="badge badge-live">Supported</span></a></li>
          <li><a href="/docs/odoo/"{active_odoo}><span class="docs-nav-link-inner"><span class="tab-icon tab-icon--odoo" aria-hidden="true"></span>Odoo</span> <span class="badge badge-live">Supported</span></a></li>
          <li><a href="/docs/flask/"{active_flask}><span class="docs-nav-link-inner"><span class="tab-icon tab-icon--flask" aria-hidden="true"></span>Flask</span> <span class="badge badge-soon">Soon</span></a></li>
        </ul>
      </div>
    </aside>

    <main class="docs-main docs-content">
      <article class="docs-prose" data-pagefind-body>
{content}
      </article>
    </main>
  </div>

  <footer class="site-footer">
    <span>Built for Python developers</span>
    <span class="footer-sep">·</span>
    <a href="https://github.com/uploadkit" target="_blank" rel="noopener">github.com/uploadkit</a>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-core.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-clike.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-python.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-bash.min.js"></script>
  <script src="/pagefind/pagefind-ui.js"></script>
  <script src="/script.js"></script>
</body>
</html>
"""

ACTIVE_KEYS = (
    "getting",
    "core",
    "patterns",
    "storage",
    "security",
    "django",
    "fastapi",
    "aiohttp",
    "odoo",
    "flask",
)


def active_attrs(current: str) -> dict[str, str]:
    return {
        f"active_{k}": ' class="active" aria-current="page"' if k == current else ""
        for k in ACTIVE_KEYS
    }


def write_page(rel: str, *, title: str, description: str, canonical: str, current: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    html = HEAD.format(
        title=title,
        description=description,
        canonical=canonical,
        content=content,
        **active_attrs(current),
    )
    path.write_text(html, encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


def code_block(filename: str, lang: str, code: str, *, console: bool = False) -> str:
    cls = "code-block code-block--console" if console else "code-block"
    escaped = (
        code.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return f"""          <figure class="{cls}">
            <figcaption class="code-block-caption">
              <code>{filename}</code>
              <button type="button" class="copy-btn" aria-label="Copy">Copy</button>
            </figcaption>
            <div class="code-block-body">
              <pre><code class="language-{lang}">{escaped}</code></pre>
            </div>
          </figure>"""


def install_tabs(prefix: str, pip: str, uv: str, poetry: str) -> str:
    return f"""          <div class="tabs nested-tabs install-tabs" data-tabs="install-{prefix}">
            <div class="tab-bar" role="tablist" aria-label="Install with">
              <button type="button" class="tab-btn active" data-tab="install-{prefix}-pip" role="tab" aria-selected="true">pip</button>
              <button type="button" class="tab-btn" data-tab="install-{prefix}-uv" role="tab" aria-selected="false">uv</button>
              <button type="button" class="tab-btn" data-tab="install-{prefix}-poetry" role="tab" aria-selected="false">poetry</button>
            </div>
            <div id="install-{prefix}-pip" class="tab-panel active" role="tabpanel">
{code_block("Shell", "bash", pip, console=True)}
            </div>
            <div id="install-{prefix}-uv" class="tab-panel" role="tabpanel">
{code_block("Shell", "bash", uv, console=True)}
            </div>
            <div id="install-{prefix}-poetry" class="tab-panel" role="tabpanel">
{code_block("Shell", "bash", poetry, console=True)}
            </div>
          </div>"""


# --- Content ---

GETTING = f"""
        <h1>Getting started</h1>
        <p class="section-lead">UploadKit is a modular, framework-independent upload pipeline for Python. Install Core, add security validators, then wire a framework adapter (or use Core directly).</p>

        <h2>Install Core</h2>
{install_tabs(
    "getting",
    "pip install uploadkit uploadkit-security\n# optional storage SDKs (not package deps):\n# pip install boto3 aioboto3",
    "uv add uploadkit uploadkit-security",
    "poetry add uploadkit uploadkit-security",
)}

        <h2>Next steps</h2>
        <ul>
          <li><a href="/docs/core/">Core reference</a> — sync <code>Uploader</code> and async <code>AsyncUploader</code></li>
          <li><a href="/docs/storage/">Storage</a> — boto3 / aioboto3 for AWS S3 and MinIO</li>
          <li><a href="/docs/patterns/">Common patterns</a> — policy, validators, errors, JSON shape</li>
          <li><a href="/docs/django/">Django</a>, <a href="/docs/fastapi/">FastAPI</a>, <a href="/docs/aiohttp/">aiohttp</a>, or <a href="/docs/odoo/">Odoo</a> — adapter glue</li>
          <li><a href="/docs/security/">Security</a> — <code>uploadkit-security</code> and libmagic</li>
        </ul>
"""

CORE_SYNC = """import boto3
from botocore.client import Config
from uploadkit import Uploader, UploadPolicy
from uploadkit_security import default_validators

class Boto3S3Storage:
    def __init__(self, *, access_key, secret_key, region="us-east-1", endpoint_url=None):
        kwargs = dict(
            service_name="s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
            config=Config(signature_version="s3v4"),
        )
        if endpoint_url:
            kwargs["endpoint_url"] = endpoint_url
        self.client = boto3.client(**kwargs)

    def put(self, *, bucket, object_name, body, content_type):
        resp = self.client.put_object(
            Bucket=bucket, Key=object_name, Body=body, ContentType=content_type,
        )
        return resp.get("ETag")

# AWS S3
storage = Boto3S3Storage(access_key="AKIA...", secret_key="...", region="eu-west-1")

# MinIO
storage = Boto3S3Storage(
    endpoint_url="http://127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
)

# Policy + validators: see Common patterns
policy = UploadPolicy(
    max_size=10 * 1024 * 1024,
    allowed_extensions=frozenset({"png", "jpg"}),
    allowed_mime_types=frozenset({"image/png", "image/jpeg"}),
    validators=default_validators(),
)
result = Uploader(policy, storage).upload(
    file, bucket="uploads", object_name="2026/file.png",
)"""

CORE_ASYNC = """from uploadkit import AsyncUploader, UploadPolicy
from uploadkit_security import default_async_validators
# from myapp.s3_async import AsyncS3Storage  # see /docs/storage/

# AWS S3
async_storage = AsyncS3Storage(
    access_key="AKIA...", secret_key="...", region="eu-west-1",
)
# MinIO
async_storage = AsyncS3Storage(
    endpoint_url="http://127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
)

policy = UploadPolicy(
    max_size=10 * 1024 * 1024,
    allowed_extensions=frozenset({"png", "jpg"}),
    allowed_mime_types=frozenset({"image/png", "image/jpeg"}),
    async_validators=default_async_validators(),
)
result = await AsyncUploader(policy, async_storage).upload(
    source,  # AsyncByteSource
    bucket="uploads",
    object_name="2026/file.png",
)"""

CORE = f"""
        <h1>Core</h1>
        <p class="section-lead">Framework-free orchestration. Choose sync <code>Uploader</code> or async streaming <code>AsyncUploader</code> — then plug any framework adapter.</p>

        <h2>Install</h2>
{install_tabs(
    "core",
    "pip install uploadkit uploadkit-security\n# optional storage SDKs (not package deps):\n# pip install boto3 aioboto3",
    "uv add uploadkit uploadkit-security",
    "poetry add uploadkit uploadkit-security",
)}

        <h2>Examples</h2>
        <p class="section-note">Shared <code>UploadPolicy</code>, validators, and error handling are documented in <a href="/docs/patterns/">Common patterns</a>.</p>

        <div class="tabs nested-tabs" data-tabs="core-inner">
          <div class="tab-bar" role="tablist" aria-label="Core examples">
            <button type="button" class="tab-btn active" data-tab="tab-core-sync" role="tab" aria-selected="true">Sync</button>
            <button type="button" class="tab-btn" data-tab="tab-core-async" role="tab" aria-selected="false">Async</button>
          </div>

          <div id="tab-core-sync" class="tab-panel active" role="tabpanel">
            <p class="section-note"><code>Boto3S3Storage</code> works for <strong>AWS S3</strong> and <strong>MinIO</strong>. Full classes and install notes: <a href="/docs/storage/">Storage</a>.</p>
{code_block("storage_sync.py", "python", CORE_SYNC)}
          </div>

          <div id="tab-core-async" class="tab-panel" role="tabpanel">
            <p class="section-note"><code>AsyncS3Storage</code> (aioboto3 multipart) — same AWS vs MinIO wiring. Full writer class: <a href="/docs/storage/">Storage</a>.</p>
{code_block("example_async.py", "python", CORE_ASYNC)}
          </div>
        </div>

        <p class="section-note">
          Storage providers:
          <a href="/docs/storage/">Storage</a>
          ·
          Docs:
          <a href="https://github.com/uploadkit/uploadkit" target="_blank" rel="noopener">uploadkit</a>
          ·
          <a href="https://github.com/uploadkit/uploadkit-security" target="_blank" rel="noopener">uploadkit-security</a>
        </p>
"""

DJANGO_VIEW = """from django.conf import settings
from django.http import JsonResponse
from uploadkit import Uploader, UploadPolicy, UploaderError
from uploadkit_django import as_uploadable, get_storage_provider, json_error_response
from uploadkit_security import default_validators

def upload_view(request):
    storage = get_storage_provider()
    policy = UploadPolicy(
        max_size=5 * 1024 * 1024,
        allowed_extensions=frozenset({"png"}),
        allowed_mime_types=frozenset({"image/png"}),
        validators=default_validators(),
    )
    uploaded = request.FILES["file"]
    try:
        result = Uploader(policy, storage).upload(
            as_uploadable(uploaded),
            bucket=settings.UPLOADKIT_BUCKET,
            object_name=uploaded.name,
        )
    except UploaderError as exc:
        return json_error_response(exc)
    return JsonResponse({
        "object_name": result.object_name,
        "sha256": result.sha256,
        "etag": result.etag,
    })"""

DJANGO_SETTINGS = """# settings.py — AWS S3
AWS_ACCESS_KEY_ID = "AKIA..."
AWS_SECRET_ACCESS_KEY = "..."
AWS_S3_REGION_NAME = "eu-west-1"
UPLOADKIT_STORAGE_PROVIDER = "myapp.storage.get_provider"
UPLOADKIT_BUCKET = "my-prod-bucket"

# settings.py — MinIO (instead of / in addition to keys)
# AWS_S3_ENDPOINT_URL = "http://127.0.0.1:9000"
# AWS_ACCESS_KEY_ID = "minioadmin"
# AWS_SECRET_ACCESS_KEY = "minioadmin"

# myapp/storage.py — Boto3S3Storage + get_provider()
# (full class in /docs/storage/)
def get_provider():
    from django.conf import settings
    return Boto3S3Storage(
        access_key=settings.AWS_ACCESS_KEY_ID,
        secret_key=settings.AWS_SECRET_ACCESS_KEY,
        region=getattr(settings, "AWS_S3_REGION_NAME", "us-east-1"),
        endpoint_url=getattr(settings, "AWS_S3_ENDPOINT_URL", None),
    )"""

DJANGO = f"""
        <h1>Django</h1>
        <p class="section-lead">Thin integration over Core. Pair with <code>uploadkit-security</code> for the default validator stack. Python 3.10–3.13, Django 4.2+.</p>

        <h2>Install</h2>
{install_tabs(
    "django",
    "pip install uploadkit-django uploadkit-security",
    "uv add uploadkit-django uploadkit-security",
    "poetry add uploadkit-django uploadkit-security",
)}

        <h2>Adapter glue</h2>
        <p class="section-note">Policy setup, validators, <code>UploaderError</code>, and the JSON response shape are shared — see <a href="/docs/patterns/">Common patterns</a>.</p>

        <div class="tabs nested-tabs" data-tabs="django-inner">
          <div class="tab-bar" role="tablist" aria-label="Django examples">
            <button type="button" class="tab-btn active" data-tab="tab-view" role="tab" aria-selected="true">View</button>
            <button type="button" class="tab-btn" data-tab="tab-settings" role="tab" aria-selected="false">Settings</button>
          </div>

          <div id="tab-view" class="tab-panel active" role="tabpanel">
            <p class="section-note">Uses <code>get_storage_provider()</code> → <code>Boto3S3Storage</code> (AWS S3 or MinIO) and <code>as_uploadable()</code>.</p>
{code_block("views.py", "python", DJANGO_VIEW)}
          </div>

          <div id="tab-settings" class="tab-panel" role="tabpanel">
            <p class="section-note">AWS: leave <code>AWS_S3_ENDPOINT_URL</code> unset. MinIO: set it to your endpoint.</p>
{code_block("settings.py + storage.py", "python", DJANGO_SETTINGS)}
          </div>
        </div>

        <p class="section-note">
          Full <code>Boto3S3Storage</code> class:
          <a href="/docs/storage/">Storage</a>
          ·
          <a href="https://github.com/uploadkit/uploadkit-django" target="_blank" rel="noopener">uploadkit-django README</a>
        </p>
"""

FASTAPI_ASYNC = """from fastapi import BackgroundTasks, FastAPI, UploadFile
from uploadkit import AsyncUploader, UploadPolicy, UploaderError
from uploadkit_fastapi import (
    as_async_source,
    background_after_upload,
    json_error_response,
)
from uploadkit_security import default_async_validators

app = FastAPI()
# AWS:
# async_storage = AsyncS3Storage(access_key="AKIA...", secret_key="...", region="eu-west-1")
# MinIO:
async_storage = AsyncS3Storage(
    endpoint_url="http://127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
)

@app.post("/upload")
async def upload(file: UploadFile, background_tasks: BackgroundTasks):
    policy = UploadPolicy(
        max_size=5 * 1024 * 1024,
        allowed_extensions=frozenset({"png"}),
        allowed_mime_types=frozenset({"image/png"}),
        async_validators=default_async_validators(),
    )
    try:
        result = await AsyncUploader(policy, async_storage).upload(
            as_async_source(file),
            bucket="uploads",
            object_name=file.filename or "object",
            after_upload=background_after_upload(background_tasks, notify),
        )
    except UploaderError as exc:
        return json_error_response(exc)
    return {
        "object_name": result.object_name,
        "sha256": result.sha256,
        "etag": result.etag,
    }"""

FASTAPI_SYNC = """from fastapi import BackgroundTasks, FastAPI, UploadFile
from uploadkit import Uploader, UploadPolicy, UploaderError
from uploadkit_fastapi import (
    as_uploadable,
    background_after_upload,
    json_error_response,
    run_sync_upload,
)
from uploadkit_security import default_validators

app = FastAPI()
# AWS: Boto3S3Storage(access_key="AKIA...", secret_key="...", region="eu-west-1")
boto3_storage = Boto3S3Storage(
    endpoint_url="http://127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
)

@app.post("/upload-sync")
async def upload_sync(file: UploadFile, background_tasks: BackgroundTasks):
    policy = UploadPolicy(
        max_size=5 * 1024 * 1024,
        allowed_extensions=frozenset({"png"}),
        allowed_mime_types=frozenset({"image/png"}),
        validators=default_validators(),
    )
    try:
        result = await run_sync_upload(
            Uploader(policy, boto3_storage),
            as_uploadable(file),
            bucket="uploads",
            object_name=file.filename or "object",
            after_upload=background_after_upload(background_tasks, notify),
        )
    except UploaderError as exc:
        return json_error_response(exc)
    return {
        "object_name": result.object_name,
        "sha256": result.sha256,
        "etag": result.etag,
    }"""

FASTAPI = f"""
        <h1>FastAPI</h1>
        <p class="section-lead">Thin FastAPI adapters over Core. Choose <strong>async streaming</strong> (<code>AsyncS3Storage</code> / aioboto3) or <strong>sync</strong> (<code>Boto3S3Storage</code> / boto3). Pair with <code>uploadkit-security</code>.</p>

        <h2>Install</h2>
{install_tabs(
    "fastapi",
    "pip install uploadkit-fastapi uploadkit-security",
    "uv add uploadkit-fastapi uploadkit-security",
    "poetry add uploadkit-fastapi uploadkit-security",
)}

        <h2>Adapter glue</h2>
        <p class="section-note">Shared policy, validators, errors, and JSON shape: <a href="/docs/patterns/">Common patterns</a>.</p>

        <div class="tabs nested-tabs" data-tabs="fastapi-inner">
          <div class="tab-bar" role="tablist" aria-label="FastAPI examples">
            <button type="button" class="tab-btn active" data-tab="tab-fastapi-async" role="tab" aria-selected="true">Async</button>
            <button type="button" class="tab-btn" data-tab="tab-fastapi-sync" role="tab" aria-selected="false">Sync</button>
          </div>

          <div id="tab-fastapi-async" class="tab-panel active" role="tabpanel">
            <p class="section-note">Copy <code>AsyncS3Storage</code> from <a href="/docs/storage/">Storage</a>. Requires <code>pip install aioboto3</code>. Uses <code>as_async_source()</code> and <code>background_after_upload()</code>.</p>
{code_block("main.py", "python", FASTAPI_ASYNC)}
          </div>

          <div id="tab-fastapi-sync" class="tab-panel" role="tabpanel">
            <p class="section-note"><code>Boto3S3Storage</code> + <code>run_sync_upload</code>. Requires <code>pip install boto3</code>. Full class: <a href="/docs/storage/">Storage</a>.</p>
{code_block("main.py", "python", FASTAPI_SYNC)}
          </div>
        </div>

        <p class="section-note">
          After-upload: <code>BackgroundTasks</code>, Celery-like <code>.delay</code>, or a plain callback.
          Full storage classes:
          <a href="/docs/storage/">Storage</a>
          ·
          <a href="https://github.com/uploadkit/uploadkit-fastapi" target="_blank" rel="noopener">uploadkit-fastapi</a>
        </p>
"""

AIOHTTP_ADAPTER = """import aiohttp
from aiohttp.multipart import BodyPartReader

class AiohttpByteSource:
    \"\"\"Adapt an aiohttp multipart part for AsyncUploader.\"\"\"

    def __init__(self, part: BodyPartReader) -> None:
        self._part = part
        self.name = part.filename
        self.size = None  # often unknown until fully read
        self.content_type = part.headers.get(
            aiohttp.hdrs.CONTENT_TYPE,
            "application/octet-stream",
        )

    async def read(self, size: int = -1) -> bytes:
        if size < 0:
            return await self._part.read(decode=False)
        chunk = await self._part.read_chunk(size)
        return chunk or b\"\""""

AIOHTTP_HANDLER = """from aiohttp import web
from uploadkit import AsyncUploader, UploadPolicy, UploaderError
from uploadkit_security import default_async_validators

from adapters import AiohttpByteSource

async def upload_handler(request: web.Request) -> web.Response:
    reader = await request.multipart()
    part = await reader.next()
    while part is not None:
        if part.name == "file" and part.filename:
            break
        part = await reader.next()
    if part is None or not part.filename:
        return web.json_response(
            {"error": "MissingFile", "message": "file field required"},
            status=400,
        )

    policy = UploadPolicy(
        max_size=5 * 1024 * 1024,
        allowed_extensions=frozenset({"png"}),
        allowed_mime_types=frozenset({"image/png"}),
        async_validators=default_async_validators(),
    )
    try:
        result = await AsyncUploader(policy, request.app["async_storage"]).upload(
            AiohttpByteSource(part),
            bucket="uploads",
            object_name=part.filename,
            after_upload=notify,  # sync, async, or Celery-like .delay
        )
    except UploaderError as exc:
        return web.json_response(
            {"error": type(exc).__name__, "message": str(exc)},
            status=400,
        )
    return web.json_response({
        "object_name": result.object_name,
        "sha256": result.sha256,
        "etag": result.etag,
    })"""

AIOHTTP_APP = """from aiohttp import web
from handlers import upload_handler
# from myapp.s3_async import AsyncS3Storage  # see /docs/storage/

async def notify(result) -> None:
    ...

# AWS:
# async_storage = AsyncS3Storage(access_key="AKIA...", secret_key="...", region="eu-west-1")
# MinIO:
async_storage = AsyncS3Storage(
    endpoint_url="http://127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
)

app = web.Application()
app["async_storage"] = async_storage
app.router.add_post("/upload", upload_handler)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)"""

AIOHTTP = f"""
        <h1>aiohttp</h1>
        <p class="section-lead">No dedicated integration package — use Core directly. Wrap aiohttp multipart parts as <code>AsyncByteSource</code> and call <code>AsyncUploader</code>. Pair with <code>uploadkit-security</code>.</p>

        <h2>Install</h2>
{install_tabs(
    "aiohttp",
    "pip install uploadkit uploadkit-security aiohttp",
    "uv add uploadkit uploadkit-security aiohttp",
    "poetry add uploadkit uploadkit-security aiohttp",
)}

        <h2>Adapter glue</h2>
        <p class="section-note">Shared policy and error conventions: <a href="/docs/patterns/">Common patterns</a>. Here the unique piece is the multipart <code>AsyncByteSource</code>.</p>

        <div class="tabs nested-tabs" data-tabs="aiohttp-inner">
          <div class="tab-bar" role="tablist" aria-label="aiohttp examples">
            <button type="button" class="tab-btn active" data-tab="tab-aiohttp-adapter" role="tab" aria-selected="true">Adapter</button>
            <button type="button" class="tab-btn" data-tab="tab-aiohttp-handler" role="tab" aria-selected="false">Handler</button>
            <button type="button" class="tab-btn" data-tab="tab-aiohttp-app" role="tab" aria-selected="false">App</button>
          </div>

          <div id="tab-aiohttp-adapter" class="tab-panel active" role="tabpanel">
            <p class="section-note">Thin <code>AsyncByteSource</code> over aiohttp’s multipart body part (<code>BodyPartReader</code>).</p>
{code_block("adapters.py", "python", AIOHTTP_ADAPTER)}
          </div>

          <div id="tab-aiohttp-handler" class="tab-panel" role="tabpanel">
            <p class="section-note">Parse multipart, find the file field, stream through <code>AsyncUploader</code>.</p>
{code_block("handlers.py", "python", AIOHTTP_HANDLER)}
          </div>

          <div id="tab-aiohttp-app" class="tab-panel" role="tabpanel">
            <p class="section-note">Use <code>AsyncS3Storage</code> from <a href="/docs/storage/">Storage</a> for AWS S3 or MinIO.</p>
{code_block("app.py", "python", AIOHTTP_APP)}
          </div>
        </div>

        <p class="section-note">
          Same Core async stack as FastAPI — only the <code>AsyncByteSource</code> adapter differs.
          Storage:
          <a href="/docs/storage/">Storage</a>
          ·
          Docs:
          <a href="https://github.com/uploadkit/uploadkit" target="_blank" rel="noopener">uploadkit</a>
        </p>
"""

ODOO_CONTROLLER = """from odoo import http
from odoo.http import request
from uploadkit import Uploader, UploadPolicy, UploaderError
from uploadkit_odoo import as_uploadable, json_error_response
from uploadkit_security import default_validators


class MyController(http.Controller):
    @http.route("/my/upload", type="http", auth="user", methods=["POST"], csrf=True)
    def upload(self, **kw):
        storage = get_provider()  # your StorageProvider factory
        policy = UploadPolicy(
            max_size=5 * 1024 * 1024,
            allowed_extensions=frozenset({"png"}),
            allowed_mime_types=frozenset({"image/png"}),
            validators=default_validators(),
        )
        uploaded = kw.get("file")
        try:
            result = Uploader(policy, storage).upload(
                as_uploadable(uploaded),
                bucket="uploads",
                object_name=uploaded.filename,
            )
        except UploaderError as exc:
            return json_error_response(exc)
        return request.make_json_response(result.as_task_kwargs())"""

ODOO_STORAGE = """# my_module/storage.py
import boto3
from botocore.client import Config
from odoo.tools import config


class Boto3S3Storage:
    def __init__(
        self,
        *,
        access_key: str,
        secret_key: str,
        region: str = "us-east-1",
        endpoint_url: str | None = None,
    ) -> None:
        kwargs: dict = {
            "service_name": "s3",
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "region_name": region,
            "config": Config(signature_version="s3v4"),
        }
        if endpoint_url:
            kwargs["endpoint_url"] = endpoint_url
        self.client = boto3.client(**kwargs)

    def put(self, *, bucket, object_name, body, content_type):
        resp = self.client.put_object(
            Bucket=bucket,
            Key=object_name,
            Body=body,
            ContentType=content_type,
        )
        return resp.get("ETag")


def get_provider():
    \"\"\"Factory used by uploadkit.storage_provider config parameter.\"\"\"
    return Boto3S3Storage(
        access_key=config.get("uploadkit_access_key", ""),
        secret_key=config.get("uploadkit_secret_key", ""),
        region=config.get("uploadkit_region", "us-east-1"),
        endpoint_url=config.get("uploadkit_endpoint_url") or None,
    )"""

ODOO_SERVICE = """# After installing the UploadKit Odoo addon:
result = env["uploadkit.service"].upload(
    file_storage,
    object_name="docs/a.pdf",
)
# result is UploadResult.as_task_kwargs()

# Or POST multipart to /uploadkit/upload (auth=user, CSRF)
# field: file  |  optional: object_name"""

ODOO = f"""
        <h1>Odoo</h1>
        <p class="section-lead">Thin integration over Core. Adapts Werkzeug <code>FileStorage</code> from Odoo controllers and maps errors to JSON. Optional Odoo 17/18 addon wires settings, a service model, and an HTTP route. Python 3.10–3.12.</p>

        <h2>Install</h2>
{install_tabs(
    "odoo",
    "pip install uploadkit-odoo uploadkit-security",
    "uv add uploadkit-odoo uploadkit-security",
    "poetry add uploadkit-odoo uploadkit-security",
)}

        <h2>Adapter glue</h2>
        <p class="section-note">Policy setup, validators, <code>UploaderError</code>, and the JSON response shape are shared — see <a href="/docs/patterns/">Common patterns</a>. Supply your own <code>StorageProvider</code>; creating <code>ir.attachment</code> records after upload is left to your module.</p>

        <div class="tabs nested-tabs" data-tabs="odoo-inner">
          <div class="tab-bar" role="tablist" aria-label="Odoo examples">
            <button type="button" class="tab-btn active" data-tab="tab-odoo-controller" role="tab" aria-selected="true">Controller</button>
            <button type="button" class="tab-btn" data-tab="tab-odoo-storage" role="tab" aria-selected="false">Storage</button>
            <button type="button" class="tab-btn" data-tab="tab-odoo-addon" role="tab" aria-selected="false">Addon</button>
          </div>

          <div id="tab-odoo-controller" class="tab-panel active" role="tabpanel">
            <p class="section-note">Uses <code>as_uploadable()</code> on Werkzeug <code>FileStorage</code> and <code>json_error_response()</code>.</p>
{code_block("controllers.py", "python", ODOO_CONTROLLER)}
          </div>

          <div id="tab-odoo-storage" class="tab-panel" role="tabpanel">
            <p class="section-note">AWS: leave <code>endpoint_url</code> unset. MinIO: set it to your endpoint. Full class also in <a href="/docs/storage/">Storage</a>.</p>
{code_block("storage.py", "python", ODOO_STORAGE)}
          </div>

          <div id="tab-odoo-addon" class="tab-panel" role="tabpanel">
            <p class="section-note">Add this repo’s <code>addons/</code> to Odoo <code>addons_path</code>, install <strong>UploadKit</strong> in Apps, then configure under <strong>Settings → UploadKit</strong> (storage factory, bucket, optional prefix / max size).</p>
{code_block("service.py", "python", ODOO_SERVICE)}
          </div>
        </div>

        <p class="section-note">
          Full <code>Boto3S3Storage</code> class:
          <a href="/docs/storage/">Storage</a>
          ·
          <a href="https://github.com/uploadkit/uploadkit-odoo" target="_blank" rel="noopener">uploadkit-odoo README</a>
        </p>
"""

FLASK = """
        <h1>Flask</h1>
        <p class="section-lead">Flask-specific adapters only. Same ecosystem boundaries as Django and FastAPI.</p>
        <p class="pkg">uploadkit-flask</p>
        <p class="section-note">Coming soon — adapters and response helpers only.</p>
"""

PATTERNS_POLICY = """from uploadkit import UploadPolicy
from uploadkit_security import default_validators, default_async_validators

# Sync pipeline
policy = UploadPolicy(
    max_size=5 * 1024 * 1024,
    allowed_extensions=frozenset({"png", "jpg"}),
    allowed_mime_types=frozenset({"image/png", "image/jpeg"}),
    validators=default_validators(),
)

# Async pipeline
async_policy = UploadPolicy(
    max_size=5 * 1024 * 1024,
    allowed_extensions=frozenset({"png"}),
    allowed_mime_types=frozenset({"image/png"}),
    async_validators=default_async_validators(),
)"""

PATTERNS_ERROR = """from uploadkit import UploaderError

# Django / FastAPI / Odoo helpers
from uploadkit_django import json_error_response  # or uploadkit_fastapi / uploadkit_odoo
try:
    result = Uploader(policy, storage).upload(...)
except UploaderError as exc:
    return json_error_response(exc)

# Manual JSON (e.g. aiohttp)
except UploaderError as exc:
    return web.json_response(
        {"error": type(exc).__name__, "message": str(exc)},
        status=400,
    )"""

PATTERNS_JSON = """{
  "object_name": "2026/file.png",
  "sha256": "…",
  "etag": "…"
}"""

PATTERNS = f"""
        <h1>Common patterns</h1>
        <p class="section-lead">Shared pieces used across Core and every framework guide. Framework pages only show adapter glue; put these conventions here once.</p>

        <h2>UploadPolicy</h2>
        <p>Size, extension, and MIME allow-lists live on the policy. Attach sync or async validators from <code>uploadkit-security</code>.</p>
{code_block("policy.py", "python", PATTERNS_POLICY)}

        <h2>Error handling</h2>
        <p>Catch <code>UploaderError</code>. Django, FastAPI, and Odoo ship <code>json_error_response</code>; aiohttp (and custom stacks) map to the same JSON shape manually.</p>
{code_block("errors.py", "python", PATTERNS_ERROR)}

        <h2>Success JSON shape</h2>
        <p>Typical success payload returned by the sample views:</p>
{code_block("response.json", "json", PATTERNS_JSON)}

        <h2>Validators</h2>
        <p>Use <code>default_validators()</code> / <code>default_async_validators()</code> from <code>uploadkit-security</code>. For MIME detection with libmagic, see the <a href="/docs/security/">Security</a> page.</p>
"""

STORAGE_SYNC = """import boto3
from botocore.client import Config


class Boto3S3Storage:
    \"\"\"S3-compatible sync storage for AWS S3 or MinIO.\"\"\"

    def __init__(
        self,
        *,
        access_key: str,
        secret_key: str,
        region: str = "us-east-1",
        endpoint_url: str | None = None,
    ) -> None:
        kwargs: dict = {
            "service_name": "s3",
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "region_name": region,
            "config": Config(signature_version="s3v4"),
        }
        if endpoint_url:
            kwargs["endpoint_url"] = endpoint_url
        self.client = boto3.client(**kwargs)

    def put(self, *, bucket, object_name, body, content_type):
        resp = self.client.put_object(
            Bucket=bucket,
            Key=object_name,
            Body=body,
            ContentType=content_type,
        )
        return resp.get("ETag")


# AWS S3
storage = Boto3S3Storage(
    access_key="AKIA...",
    secret_key="...",
    region="eu-west-1",
)

# MinIO (local default)
storage = Boto3S3Storage(
    endpoint_url="http://127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    region="us-east-1",
)"""

STORAGE_ASYNC = """from __future__ import annotations

import aioboto3
from botocore.client import Config

_PART_SIZE = 5 * 1024 * 1024  # 5 MiB


class AsyncS3Writer:
    def __init__(self, client, *, bucket: str, object_name: str, content_type: str) -> None:
        self._client = client
        self._bucket = bucket
        self._key = object_name
        self._content_type = content_type
        self._upload_id: str | None = None
        self._parts: list[dict] = []
        self._buffer = bytearray()
        self._part_number = 1

    async def _ensure_upload(self) -> None:
        if self._upload_id is not None:
            return
        resp = await self._client.create_multipart_upload(
            Bucket=self._bucket,
            Key=self._key,
            ContentType=self._content_type,
        )
        self._upload_id = resp["UploadId"]

    async def _flush_part(self, data: bytes) -> None:
        await self._ensure_upload()
        assert self._upload_id is not None
        resp = await self._client.upload_part(
            Bucket=self._bucket,
            Key=self._key,
            PartNumber=self._part_number,
            UploadId=self._upload_id,
            Body=data,
        )
        self._parts.append({"ETag": resp["ETag"], "PartNumber": self._part_number})
        self._part_number += 1

    async def write(self, chunk: bytes) -> None:
        self._buffer.extend(chunk)
        while len(self._buffer) >= _PART_SIZE:
            part = bytes(self._buffer[:_PART_SIZE])
            del self._buffer[:_PART_SIZE]
            await self._flush_part(part)

    async def abort(self) -> None:
        if self._upload_id is None:
            return
        await self._client.abort_multipart_upload(
            Bucket=self._bucket,
            Key=self._key,
            UploadId=self._upload_id,
        )
        self._upload_id = None

    async def complete(self) -> str | None:
        if self._buffer:
            await self._flush_part(bytes(self._buffer))
            self._buffer.clear()
        if self._upload_id is None:
            # empty object
            resp = await self._client.put_object(
                Bucket=self._bucket,
                Key=self._key,
                Body=b"",
                ContentType=self._content_type,
            )
            return resp.get("ETag")
        resp = await self._client.complete_multipart_upload(
            Bucket=self._bucket,
            Key=self._key,
            UploadId=self._upload_id,
            MultipartUpload={"Parts": self._parts},
        )
        self._upload_id = None
        return resp.get("ETag")


class AsyncS3Storage:
    \"\"\"S3-compatible async storage for AWS S3 or MinIO.\"\"\"

    def __init__(
        self,
        *,
        access_key: str,
        secret_key: str,
        region: str = "us-east-1",
        endpoint_url: str | None = None,
    ) -> None:
        self._session = aioboto3.Session()
        self._client_kwargs: dict = {
            "service_name": "s3",
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "region_name": region,
            "config": Config(signature_version="s3v4"),
        }
        if endpoint_url:
            self._client_kwargs["endpoint_url"] = endpoint_url
        self._cm = None
        self._client = None

    async def _get_client(self):
        if self._client is None:
            self._cm = self._session.client(**self._client_kwargs)
            self._client = await self._cm.__aenter__()
        return self._client

    async def open_write(self, *, bucket: str, object_name: str, content_type: str):
        client = await self._get_client()
        return AsyncS3Writer(
            client,
            bucket=bucket,
            object_name=object_name,
            content_type=content_type,
        )


# AWS S3
async_storage = AsyncS3Storage(
    access_key="AKIA...",
    secret_key="...",
    region="eu-west-1",
)

# MinIO
async_storage = AsyncS3Storage(
    endpoint_url="http://127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
)"""

STORAGE = f"""
        <h1>Storage</h1>
        <p class="section-lead">UploadKit does <strong>not</strong> ship storage clients. You implement <code>StorageProvider</code> (sync) or <code>AsyncStorageProvider</code> (async) once — the same classes work for <strong>AWS S3</strong> (omit <code>endpoint_url</code>) and <strong>MinIO</strong> (set <code>endpoint_url</code>) via <code>boto3</code> / <code>aioboto3</code>.</p>

        <h2>Install</h2>
        <p class="section-note">These are app dependencies, not UploadKit package deps.</p>
{install_tabs(
    "storage",
    "pip install boto3          # sync AWS S3 / MinIO\npip install aioboto3       # async AWS S3 / MinIO",
    "uv add boto3        # sync\nuv add aioboto3     # async",
    "poetry add boto3    # sync\npoetry add aioboto3 # async",
)}

        <h2>Protocols</h2>
        <p>Sync pipelines call <code>StorageProvider.put(*, bucket, object_name, body, content_type)</code> and expect an etag (or <code>None</code>).</p>
        <p>Async pipelines call <code>AsyncStorageProvider.open_write(...)</code>, then stream through <code>AsyncObjectWriter</code>: <code>write</code> → <code>complete</code> (or <code>abort</code> on failure).</p>

        <h2>Examples</h2>
        <p class="section-lead">Copy these classes into your app. Wire them into <code>Uploader</code> / <code>AsyncUploader</code> as shown on the <a href="/docs/core/">Core</a> page.</p>
        <div class="tabs nested-tabs" data-tabs="storage-examples">
          <div class="tab-bar" role="tablist" aria-label="Storage examples">
            <button type="button" class="tab-btn active" data-tab="tab-storage-sync" role="tab" aria-selected="true">Sync (boto3)</button>
            <button type="button" class="tab-btn" data-tab="tab-storage-async" role="tab" aria-selected="false">Async (aioboto3)</button>
          </div>
          <div id="tab-storage-sync" class="tab-panel active" role="tabpanel">
            <p class="section-note"><code>Boto3S3Storage</code> implements <code>StorageProvider</code>. Requires <code>pip install boto3</code>.</p>
{code_block("s3_sync.py", "python", STORAGE_SYNC)}
          </div>
          <div id="tab-storage-async" class="tab-panel" role="tabpanel">
            <p class="section-note">Multipart streaming writer (5 MiB part size — S3/MinIO rule except the last part). Requires <code>pip install aioboto3</code>.</p>
{code_block("s3_async.py", "python", STORAGE_ASYNC)}
          </div>
        </div>

        <h2>AWS S3 vs MinIO</h2>
        <p>Same class for both. Leave <code>endpoint_url</code> unset for AWS S3. For MinIO, set it to your API URL (local default <code>http://127.0.0.1:9000</code> with <code>minioadmin</code> / <code>minioadmin</code>).</p>
        <p class="section-note">Django settings use the same toggle via <code>AWS_S3_ENDPOINT_URL</code> — see the <a href="/docs/django/">Django</a> guide. Odoo uses <code>odoo.tools.config</code> keys — see the <a href="/docs/odoo/">Odoo</a> guide.</p>

        <h2>Frameworks</h2>
        <p>Adapter glue only — storage classes stay in your app:</p>
        <ul>
          <li><a href="/docs/django/">Django</a> — <code>UPLOADKIT_STORAGE_PROVIDER</code> factory + <code>get_storage_provider()</code></li>
          <li><a href="/docs/fastapi/">FastAPI</a> — async streaming or sync via <code>run_sync_upload</code></li>
          <li><a href="/docs/aiohttp/">aiohttp</a> — store the provider on <code>app["async_storage"]</code></li>
          <li><a href="/docs/odoo/">Odoo</a> — dotted-path factory + optional addon settings</li>
        </ul>

        <h2>Testing</h2>
        <p>Use <code>FakeStorageProvider</code> from <code>uploadkit-testing</code> so tests never hit S3 or MinIO.</p>

        <p class="section-note">
          Shared policy and error conventions:
          <a href="/docs/patterns/">Common patterns</a>.
          GitHub copy of these samples:
          <a href="https://github.com/uploadkit/uploadkit#storage-examples-aws-s3-and-minio" target="_blank" rel="noopener">Core README</a>.
        </p>
"""

SECURITY_DEFAULTS_SYNC = """from uploadkit import UploadPolicy
from uploadkit_security import default_validators

policy = UploadPolicy(
    max_size=5 * 1024 * 1024,
    allowed_extensions=frozenset({"png", "jpg"}),
    allowed_mime_types=frozenset({"image/png", "image/jpeg"}),
    validators=default_validators(),
)"""

SECURITY_DEFAULTS_ASYNC = """from uploadkit import UploadPolicy
from uploadkit_security import default_async_validators

policy = UploadPolicy(
    max_size=5 * 1024 * 1024,
    allowed_extensions=frozenset({"png", "jpg"}),
    allowed_mime_types=frozenset({"image/png", "image/jpeg"}),
    async_validators=default_async_validators(),
)"""

SECURITY_CUSTOMIZE_SYNC = """from uploadkit import UploadPolicy
from uploadkit_security import (
    ChecksumValidator,
    FileNameValidator,
    FileSizeValidator,
    default_validators,
)

# Drop checksum from the full stack
validators = default_validators(exclude=ChecksumValidator)

# Keep only size + filename
validators = default_validators(
    include=(FileSizeValidator, FileNameValidator),
)

policy = UploadPolicy(
    max_size=5 * 1024 * 1024,
    validators=validators,
)"""

SECURITY_CUSTOMIZE_ASYNC = """from uploadkit import UploadPolicy
from uploadkit_security import (
    AsyncChecksumValidator,
    AsyncFileNameValidator,
    AsyncFileSizeValidator,
    default_async_validators,
)

# Drop checksum from the full stack
async_validators = default_async_validators(exclude=AsyncChecksumValidator)

# Keep only size + filename
async_validators = default_async_validators(
    include=(AsyncFileSizeValidator, AsyncFileNameValidator),
)

policy = UploadPolicy(
    max_size=5 * 1024 * 1024,
    async_validators=async_validators,
)"""

SECURITY_MIME_SYNC = """from uploadkit import UploadPolicy
from uploadkit_security import detect_mime_type, default_validators

# Requires: pip install 'uploadkit-security[magic]' + OS libmagic
head = open("photo.png", "rb").read(2048)
print(detect_mime_type(head, "photo.png"))  # e.g. "image/png"

policy = UploadPolicy(
    max_size=5 * 1024 * 1024,
    allowed_extensions=frozenset({"png", "pdf"}),
    allowed_mime_types=frozenset({"image/png", "application/pdf"}),
    validators=default_validators(),  # MimeTypeValidator uses detect_mime_type
)"""

SECURITY_MIME_ASYNC = """from uploadkit import UploadPolicy
from uploadkit_security import detect_mime_type, default_async_validators

# Requires: pip install 'uploadkit-security[magic]' + OS libmagic
head = open("photo.png", "rb").read(2048)
print(detect_mime_type(head, "photo.png"))  # e.g. "image/png"

policy = UploadPolicy(
    max_size=5 * 1024 * 1024,
    allowed_extensions=frozenset({"png", "pdf"}),
    allowed_mime_types=frozenset({"image/png", "application/pdf"}),
    async_validators=default_async_validators(),  # AsyncMimeTypeValidator
)"""

SECURITY_FILENAME_CHECKSUM_SYNC = """from uploadkit import UploadPolicy
from uploadkit_security import (
    ChecksumValidator,
    FileNameValidator,
    default_validators,
    sanitize_filename,
)

print(sanitize_filename("../../evil name!!.txt"))  # "evil name__.txt"

# Filename hardening only
validators = default_validators(include=(FileNameValidator,))

# Checksum only — result.sha256 after upload
validators = default_validators(include=(ChecksumValidator,))

policy = UploadPolicy(validators=validators)"""

SECURITY_FILENAME_CHECKSUM_ASYNC = """from uploadkit import UploadPolicy
from uploadkit_security import (
    AsyncChecksumValidator,
    AsyncFileNameValidator,
    default_async_validators,
    sanitize_filename,
)

print(sanitize_filename("../../evil name!!.txt"))  # "evil name__.txt"

# Filename hardening only
async_validators = default_async_validators(include=(AsyncFileNameValidator,))

# Checksum only — result.sha256 after upload
async_validators = default_async_validators(include=(AsyncChecksumValidator,))

policy = UploadPolicy(async_validators=async_validators)"""

SECURITY = f"""
        <h1>Security</h1>
        <p class="section-lead"><code>uploadkit-security</code> provides size, extension, MIME, filename, and checksum validators (sync + async). Pair it with Core or any framework adapter.</p>

        <h2>Install</h2>
{install_tabs(
    "security",
    "pip install uploadkit-security",
    "uv add uploadkit-security",
    "poetry add uploadkit-security",
)}

        <h2>System requirements — libmagic</h2>
        <p>
          For comprehensive MIME detection, install OS <code>libmagic</code> and
          <code>uploadkit-security[magic]</code> (uses <code>python-magic</code>).
          Without it, a built-in signature checker covers common types.
          See
          <a href="https://github.com/uploadkit/uploadkit-security" target="_blank" rel="noopener">uploadkit-security</a>.
        </p>
        <div class="os-package-table" role="table" aria-label="libmagic packages by OS">
          <div class="os-package-row" role="row">
            <span class="os-name">Ubuntu / Debian</span>
            <code>libmagic1</code>
          </div>
          <div class="os-package-row" role="row">
            <span class="os-name">Fedora / RHEL</span>
            <code>file-libs</code>
          </div>
          <div class="os-package-row" role="row">
            <span class="os-name">Alpine</span>
            <code>libmagic</code>
          </div>
          <div class="os-package-row" role="row">
            <span class="os-name">macOS (Homebrew)</span>
            <code>libmagic</code>
          </div>
        </div>

        <div class="tabs nested-tabs install-tabs" data-tabs="install-libmagic">
          <div class="tab-bar" role="tablist" aria-label="Install libmagic">
            <button type="button" class="tab-btn active" data-tab="install-libmagic-debian" role="tab" aria-selected="true">Debian</button>
            <button type="button" class="tab-btn" data-tab="install-libmagic-fedora" role="tab" aria-selected="false">Fedora</button>
            <button type="button" class="tab-btn" data-tab="install-libmagic-alpine" role="tab" aria-selected="false">Alpine</button>
            <button type="button" class="tab-btn" data-tab="install-libmagic-macos" role="tab" aria-selected="false">macOS</button>
          </div>
          <div id="install-libmagic-debian" class="tab-panel active" role="tabpanel">
{code_block("Shell", "bash", "sudo apt install libmagic1\npip install 'uploadkit-security[magic]'", console=True)}
          </div>
          <div id="install-libmagic-fedora" class="tab-panel" role="tabpanel">
{code_block("Shell", "bash", "sudo dnf install file-libs\npip install 'uploadkit-security[magic]'", console=True)}
          </div>
          <div id="install-libmagic-alpine" class="tab-panel" role="tabpanel">
{code_block("Shell", "bash", "sudo apk add libmagic\npip install 'uploadkit-security[magic]'", console=True)}
          </div>
          <div id="install-libmagic-macos" class="tab-panel" role="tabpanel">
{code_block("Shell", "bash", "brew install libmagic\npip install 'uploadkit-security[magic]'", console=True)}
          </div>
        </div>
        <p class="section-note">Optional: prefer <code>uv add 'uploadkit-security[magic]'</code> or <code>poetry add uploadkit-security -E magic</code>.</p>

        <h2>Examples</h2>
        <p class="section-lead">Attach validators on <code>UploadPolicy</code>. Sync pipelines use <code>validators</code>; async pipelines use <code>async_validators</code>.</p>

        <h3>Default stack</h3>
        <p>Size → extension → MIME → filename → checksum. Policy allow-lists are read by the validators.</p>
        <div class="tabs nested-tabs" data-tabs="security-defaults">
          <div class="tab-bar" role="tablist" aria-label="Default stack examples">
            <button type="button" class="tab-btn active" data-tab="tab-security-defaults-sync" role="tab" aria-selected="true">Sync</button>
            <button type="button" class="tab-btn" data-tab="tab-security-defaults-async" role="tab" aria-selected="false">Async</button>
          </div>
          <div id="tab-security-defaults-sync" class="tab-panel active" role="tabpanel">
{code_block("policy_sync.py", "python", SECURITY_DEFAULTS_SYNC)}
          </div>
          <div id="tab-security-defaults-async" class="tab-panel" role="tabpanel">
{code_block("policy_async.py", "python", SECURITY_DEFAULTS_ASYNC)}
          </div>
        </div>

        <h3>Customize the stack</h3>
        <p>Use <code>include</code>, <code>exclude</code>, and <code>extra</code> on <code>default_validators()</code> / <code>default_async_validators()</code>.</p>
        <div class="tabs nested-tabs" data-tabs="security-customize">
          <div class="tab-bar" role="tablist" aria-label="Customize stack examples">
            <button type="button" class="tab-btn active" data-tab="tab-security-customize-sync" role="tab" aria-selected="true">Sync</button>
            <button type="button" class="tab-btn" data-tab="tab-security-customize-async" role="tab" aria-selected="false">Async</button>
          </div>
          <div id="tab-security-customize-sync" class="tab-panel active" role="tabpanel">
{code_block("customize_sync.py", "python", SECURITY_CUSTOMIZE_SYNC)}
          </div>
          <div id="tab-security-customize-async" class="tab-panel" role="tabpanel">
{code_block("customize_async.py", "python", SECURITY_CUSTOMIZE_ASYNC)}
          </div>
        </div>

        <h3>MIME detection</h3>
        <p><code>MimeTypeValidator</code> / <code>AsyncMimeTypeValidator</code> call <code>detect_mime_type</code>. With <code>uploadkit-security[magic]</code> and OS libmagic installed, sniffing uses <code>python-magic</code>; otherwise a built-in signature table covers common types.</p>
        <div class="tabs nested-tabs" data-tabs="security-mime">
          <div class="tab-bar" role="tablist" aria-label="MIME detection examples">
            <button type="button" class="tab-btn active" data-tab="tab-security-mime-sync" role="tab" aria-selected="true">Sync</button>
            <button type="button" class="tab-btn" data-tab="tab-security-mime-async" role="tab" aria-selected="false">Async</button>
          </div>
          <div id="tab-security-mime-sync" class="tab-panel active" role="tabpanel">
{code_block("mime_sync.py", "python", SECURITY_MIME_SYNC)}
          </div>
          <div id="tab-security-mime-async" class="tab-panel" role="tabpanel">
{code_block("mime_async.py", "python", SECURITY_MIME_ASYNC)}
          </div>
        </div>

        <h3>Filename and checksum</h3>
        <p>Harden names with <code>FileNameValidator</code> / <code>sanitize_filename</code>. Compute SHA-256 with <code>ChecksumValidator</code> so <code>result.sha256</code> is set after upload.</p>
        <div class="tabs nested-tabs" data-tabs="security-filename-checksum">
          <div class="tab-bar" role="tablist" aria-label="Filename and checksum examples">
            <button type="button" class="tab-btn active" data-tab="tab-security-filename-sync" role="tab" aria-selected="true">Sync</button>
            <button type="button" class="tab-btn" data-tab="tab-security-filename-async" role="tab" aria-selected="false">Async</button>
          </div>
          <div id="tab-security-filename-sync" class="tab-panel active" role="tabpanel">
{code_block("filename_checksum_sync.py", "python", SECURITY_FILENAME_CHECKSUM_SYNC)}
          </div>
          <div id="tab-security-filename-async" class="tab-panel" role="tabpanel">
{code_block("filename_checksum_async.py", "python", SECURITY_FILENAME_CHECKSUM_ASYNC)}
          </div>
        </div>

        <p class="section-note">
          Shared policy and error conventions:
          <a href="/docs/patterns/">Common patterns</a>.
          Full reference:
          <a href="https://github.com/uploadkit/uploadkit-security" target="_blank" rel="noopener">uploadkit-security README</a>.
        </p>
"""

def main() -> None:
    pages = [
        ("docs/index.html", "Getting started — UploadKit", "Install UploadKit and choose a framework guide.", "/docs/", "getting", GETTING),
        ("docs/core/index.html", "Core — UploadKit", "Framework-free upload orchestration with Uploader and AsyncUploader.", "/docs/core/", "core", CORE),
        ("docs/django/index.html", "Django — UploadKit", "Django adapters and response helpers for UploadKit.", "/docs/django/", "django", DJANGO),
        ("docs/fastapi/index.html", "FastAPI — UploadKit", "FastAPI adapters, BackgroundTasks, and async/sync helpers.", "/docs/fastapi/", "fastapi", FASTAPI),
        ("docs/aiohttp/index.html", "aiohttp — UploadKit", "Use UploadKit Core directly with aiohttp multipart.", "/docs/aiohttp/", "aiohttp", AIOHTTP),
        ("docs/odoo/index.html", "Odoo — UploadKit", "Odoo adapters, Werkzeug FileStorage glue, and optional Odoo 17/18 addon.", "/docs/odoo/", "odoo", ODOO),
        ("docs/flask/index.html", "Flask — UploadKit", "Flask adapters coming soon.", "/docs/flask/", "flask", FLASK),
        ("docs/patterns/index.html", "Common patterns — UploadKit", "Shared UploadPolicy, validators, errors, and JSON response shape.", "/docs/patterns/", "patterns", PATTERNS),
        ("docs/storage/index.html", "Storage — UploadKit", "BYO S3-compatible storage with boto3 and aioboto3 for AWS S3 and MinIO.", "/docs/storage/", "storage", STORAGE),
        ("docs/security/index.html", "Security — UploadKit", "uploadkit-security validators and libmagic system requirements.", "/docs/security/", "security", SECURITY),
    ]
    for rel, title, desc, canonical, current, content in pages:
        write_page(rel, title=title, description=desc, canonical=canonical, current=current, content=content)


if __name__ == "__main__":
    main()
