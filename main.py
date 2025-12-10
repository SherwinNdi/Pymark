#!/usr/bin/env python3
"""Convert a Markdown file to a styled PDF using WeasyPrint.

Includes a small Flask-powered web UI for live preview and PDF export.
"""
from __future__ import annotations

import io
import argparse
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

try:
    from markdown import markdown
except ImportError:  # pragma: no cover
    print("Missing dependency: markdown. Install with `pip install -r requirements.txt`.")
    sys.exit(1)

try:
    from weasyprint import CSS, HTML
except ImportError:  # pragma: no cover
    print("Missing dependency: WeasyPrint. Install with `pip install -r requirements.txt`.")
    sys.exit(1)

try:  # Imported lazily to keep CLI fast even if Flask is absent.
    from flask import Flask, jsonify, request, send_file
except ImportError:  # pragma: no cover
    Flask = None  # type: ignore
    jsonify = request = send_file = None  # type: ignore

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None

MAX_FETCH_BYTES = 1_000_000  # 1 MB guardrail for remote fetch

DEFAULT_CSS = """
@page {
  size: A4;
  margin: 1in;
}

body {
  font-family: "Helvetica", "Arial", sans-serif;
  line-height: 1.6;
  color: #222;
}

h1, h2, h3, h4, h5, h6 {
  font-weight: 700;
  color: #111;
  margin-top: 1.4em;
  margin-bottom: 0.3em;
}

p {
  margin: 0.4em 0 0.8em 0;
}

code {
  font-family: "SFMono-Regular", "Consolas", "Liberation Mono", monospace;
  background: #f5f5f5;
  padding: 0.1em 0.3em;
  border-radius: 4px;
}

pre {
  background: #f5f5f5;
  padding: 0.8em;
  border-radius: 6px;
  overflow: auto;
}

pre code {
  padding: 0;
  background: transparent;
}

a {
  color: #0b6bd3;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

blockquote {
  border-left: 4px solid #ddd;
  padding-left: 0.8em;
  color: #555;
}

ul, ol {
  margin: 0.4em 0 0.8em 1.4em;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 1em 0;
}

td, th {
  border: 1px solid #ddd;
  padding: 0.6em;
}

th {
  background: #f2f2f2;
  text-align: left;
}
"""

HTML_TEMPLATE = """<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <title>{title}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" />
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
</head>
<body>
{body}
<script>
  document.addEventListener("DOMContentLoaded", function() {{
    if (window.renderMathInElement) {{
      renderMathInElement(document.body, {{
        delimiters: [
          {{left: '$$', right: '$$', display: true}},
          {{left: '$', right: '$', display: false}},
          {{left: '\\\\[', right: '\\\\]', display: true}},
          {{left: '\\\\(', right: '\\\\)', display: false}}
        ],
        throwOnError: false
      }});
    }}
  }});
</script>
</body>
</html>
"""


def markdown_to_html(markdown_text: str) -> str:
    return markdown(markdown_text, extensions=["extra", "tables", "fenced_code"])


def markdown_to_pdf_bytes(markdown_text: str, css_text: str | None, title: str) -> bytes:
    """Convert markdown to PDF with math rendering support.
    
    Note: WeasyPrint doesn't support JavaScript, so KaTeX won't render in PDFs.
    For proper math rendering in PDFs, consider using a headless browser approach.
    This implementation includes KaTeX for the HTML preview but PDFs will show
    LaTeX source code. For production use, integrate Selenium/Playwright for
    JavaScript-rendered PDFs.
    """
    html_body = markdown_to_html(markdown_text)
    html = HTML_TEMPLATE.format(title=title, body=html_body)
    stylesheets = [CSS(string=css_text or DEFAULT_CSS)]
    buffer = io.BytesIO()
    HTML(string=html).write_pdf(buffer, stylesheets=stylesheets)
    return buffer.getvalue()


def fetch_remote_markdown(url: str, timeout: float = 6.0) -> str:
    if requests is None:  # pragma: no cover
        raise RuntimeError("requests is not installed. Install with `pip install -r requirements.txt`.")

    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError("Only http/https URLs are allowed")

    resp = requests.get(url, stream=True, timeout=timeout)
    resp.raise_for_status()

    total = 0
    chunks: list[bytes] = []
    for chunk in resp.iter_content(chunk_size=8192):
        if chunk:
            total += len(chunk)
            if total > MAX_FETCH_BYTES:
                raise ValueError("Remote file is too large (limit 1 MB)")
            chunks.append(chunk)

    content_bytes = b"".join(chunks)
    encoding = resp.encoding or "utf-8"
    return content_bytes.decode(encoding, errors="replace")


def render_markdown_to_pdf(md_path: Path, pdf_path: Path, css_path: Path | None, title: str) -> None:
    if not md_path.is_file():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    if css_path is not None and not css_path.is_file():
        raise FileNotFoundError(f"CSS file not found: {css_path}")

    markdown_text = md_path.read_text(encoding="utf-8")
    html_body = markdown_to_html(markdown_text)
    html = HTML_TEMPLATE.format(title=title, body=html_body)

    stylesheets = [CSS(filename=str(css_path))] if css_path else [CSS(string=DEFAULT_CSS)]

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(md_path.parent)).write_pdf(str(pdf_path), stylesheets=stylesheets)


def create_app() -> Any:
    if Flask is None:  # pragma: no cover
        raise RuntimeError("Flask is not installed. Install with `pip install -r requirements.txt`.")

    app = Flask(__name__, static_folder="static", static_url_path="")

    @app.get("/")
    def index():  # type: ignore
        return app.send_static_file("index.html")

    @app.get("/health")
    def health():  # type: ignore
        return {"status": "ok"}

    @app.post("/export")
    def export_pdf():  # type: ignore
        data = request.get_json(silent=True) or {}
        markdown_text = data.get("markdown", "")
        title = data.get("title") or "Document"
        css_text = data.get("css")

        if not isinstance(markdown_text, str) or not markdown_text.strip():
            return jsonify({"error": "markdown is required"}), 400

        pdf_bytes = markdown_to_pdf_bytes(markdown_text, css_text, title)
        buffer = io.BytesIO(pdf_bytes)
        buffer.seek(0)

        return send_file(
            buffer,
            mimetype="application/pdf",
            as_attachment=True,
            download_name=f"{title or 'document'}.pdf",
        )

    @app.post("/fetch-url")
    def fetch_url():  # type: ignore
        data = request.get_json(silent=True) or {}
        url = data.get("url", "")

        if not isinstance(url, str) or not url.strip():
            return jsonify({"error": "url is required"}), 400

        try:
            text = fetch_remote_markdown(url.strip())
        except Exception as exc:  # pragma: no cover
            return jsonify({"error": str(exc)}), 400

        return jsonify({"markdown": text})

    @app.post("/render-html")
    def render_html():  # type: ignore
        data = request.get_json(silent=True) or {}
        markdown_text = data.get("markdown", "")
        title = data.get("title") or "Document"
        css_text = data.get("css")

        if not isinstance(markdown_text, str) or not markdown_text.strip():
            return jsonify({"error": "markdown is required"}), 400

        html_body = markdown_to_html(markdown_text)
        css_for_html = css_text or DEFAULT_CSS
        
        # Create standalone HTML with embedded styles
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    {css_for_html}
  </style>
</head>
<body>
{html_body}
</body>
</html>"""

        return jsonify({"html": full_html})

    return app


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render a Markdown file to PDF using WeasyPrint.")
    parser.add_argument("input", type=Path, nargs="?", help="Path to the source Markdown file")
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="Optional output PDF path (defaults to input basename with .pdf)",
    )
    parser.add_argument(
        "--css",
        dest="css",
        type=Path,
        help="Optional CSS file to style the PDF (defaults to built-in style)",
    )
    parser.add_argument(
        "--title",
        dest="title",
        help="Document title (defaults to the Markdown filename)",
    )
    parser.add_argument(
        "--serve",
        dest="serve",
        action="store_true",
        help="Launch the web interface instead of running the CLI",
    )
    parser.add_argument("--host", default="127.0.0.1", help="Host for --serve (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5000, help="Port for --serve (default: 5000)")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.serve:
        app = create_app()
        app.run(host=args.host, port=args.port, debug=False)
        return 0

    if args.input is None:
        parser.error("input is required unless --serve is provided")

    md_path: Path = args.input
    output_path: Path = args.output if args.output else md_path.with_suffix(".pdf")
    css_path: Path | None = args.css
    title = args.title or md_path.stem

    try:
        render_markdown_to_pdf(md_path, output_path, css_path, title)
    except Exception as exc:  # pragma: no cover - simple CLI surface
        parser.error(str(exc))
        return 1

    print(f"Wrote PDF to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
