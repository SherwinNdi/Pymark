# md_to_pdf

Simple CLI to render a Markdown file to PDF using Python, Markdown, and WeasyPrint.

Now also includes a modern web interface with live preview and one-click PDF export.

## Setup

```bash
pip install -r requirements.txt
```

> WeasyPrint relies on system libraries (Cairo, Pango, GDK-PixBuf). On macOS you can install them via Homebrew if needed:
>
> ```bash
> brew install cairo pango gdk-pixbuf libffi
> ```

## Usage

```bash
python main.py path/to/input.md path/to/output.pdf
```

Options:

- `--css custom.css` to supply your own stylesheet.
- `--title "Custom Title"` to override the document title (defaults to the Markdown filename).
- If `output.pdf` is omitted, it defaults to the input filename with a `.pdf` extension.

Example:

```bash
python main.py README.md README.pdf --title "Project Docs"
```

## Notes

- Relative image paths in your Markdown are resolved from the Markdown file's directory.
- The script ships with a sensible default stylesheet; bring your own CSS for brand-specific styling.

## Web UI (live preview + export)

Start the web interface:

```bash
python main.py --serve --port 5000
```

Then open `http://127.0.0.1:5000` in your browser. You can:

- Toggle between split view and focus mode (editor-only).
- Live-preview Markdown with syntax highlighting and tables.
- Download your `.md` draft.
- Export to PDF via the backend (WeasyPrint).
- Import from local `.md` files or fetch a Markdown file from a URL.

> Tip: the browser autosaves drafts locally (via localStorage). Use the bottom buttons to persist files explicitly.
