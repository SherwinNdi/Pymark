const editor = document.getElementById("editor");
const preview = document.getElementById("preview");
const titleInput = document.getElementById("doc-title");
const workspace = document.getElementById("workspace");
const toggleLayoutBtn = document.getElementById("toggle-layout");
const saveMdBtn = document.getElementById("save-md");
const savePdfBtn = document.getElementById("save-pdf");
const exportBtn = document.getElementById("export-btn");
const exportHtmlBtn = document.getElementById("export-html");
const charCount = document.getElementById("char-count");
const wordCount = document.getElementById("word-count");
const menuItems = document.querySelectorAll(".menu-item");
const uploadBtn = document.getElementById("upload-btn");
const fileInput = document.getElementById("file-input");
const urlInput = document.getElementById("url-input");
const urlBtn = document.getElementById("url-btn");

const STORAGE_KEY = "md_to_pdf_draft";
const TITLE_KEY = "md_to_pdf_title";

let isSyncScrolling = false; // Prevent infinite scroll loops

marked.setOptions({ gfm: true, breaks: true });

const sample = `# Welcome to md → pdf

Use **Markdown** on the left. Toggle between split and focus modes from the top bar. 

- Live preview updates instantly
- Download your .md or export a PDF
- Images and links render inline

## Quick tips

1. Use headings to build structure
2. Add lists, code blocks, and quotes
3. Hit "Save & Export PDF" when you're ready
`;

function loadDraft() {
  const saved = localStorage.getItem(STORAGE_KEY);
  const savedTitle = localStorage.getItem(TITLE_KEY);
  editor.value = saved ?? sample;
  titleInput.value = savedTitle ?? "Untitled document";
}

function persistDraft() {
  localStorage.setItem(STORAGE_KEY, editor.value);
  localStorage.setItem(TITLE_KEY, titleInput.value);
}

function renderPreview() {
  const raw = editor.value || "";
  
  // Protect math expressions from Markdown parser
  const mathPlaceholders = [];
  let processedText = raw;
  
  // Replace display math ($$...$$) with placeholders
  processedText = processedText.replace(/\$\$([\s\S]*?)\$\$/g, (match, content) => {
    const id = mathPlaceholders.length;
    mathPlaceholders.push({ type: 'display', content: content });
    return `<!--MATH_DISPLAY_${id}-->`;
  });
  
  // Replace inline math \(...\) with placeholders
  // Match literal backslash-parenthesis patterns
  processedText = processedText.replace(/\\\(([^\)]*(?:\\\([^\)]*\\\))?[^\)]*)\\\)/g, (match, content) => {
    const id = mathPlaceholders.length;
    mathPlaceholders.push({ type: 'inline', content: content });
    return `<!--MATH_INLINE_${id}-->`;
  });
  
  // Parse markdown
  let html = marked.parse(processedText);
  
  // Restore math expressions as proper HTML with data attributes
  mathPlaceholders.forEach((math, id) => {
    const comment = math.type === 'display' 
      ? `<!--MATH_DISPLAY_${id}-->`
      : `<!--MATH_INLINE_${id}-->`;
    
    const replacement = math.type === 'display'
      ? `<span class="math-display" data-math="display">$$${math.content}$$</span>`
      : `<span class="math-inline" data-math="inline">\\(${math.content}\\)</span>`;
    
    html = html.replace(comment, replacement);
  });
  
  preview.innerHTML = DOMPurify.sanitize(html, { 
    USE_PROFILES: { html: true },
    ADD_TAGS: ['span'],
    ADD_ATTR: ['class', 'data-math']
  });
  
  // Render math with KaTeX
  if (window.renderMathInElement) {
    try {
      renderMathInElement(preview, {
        delimiters: [
          {left: '$$', right: '$$', display: true},
          {left: '\\(', right: '\\)', display: false}
        ],
        throwOnError: false,
        trust: true,
        strict: false,
        ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      });
    } catch (err) {
      console.warn('KaTeX rendering error:', err);
    }
  }
  
  const chars = raw.length;
  const words = raw.trim() ? raw.trim().split(/\s+/).length : 0;
  charCount.textContent = `${chars} chars`;
  wordCount.textContent = `${words} words`;
}

async function exportPdf() {
  const title = titleInput.value.trim() || "document";
  const payload = { markdown: editor.value, title };
  setBusy(true);
  try {
    const res = await fetch("/export", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!res.ok) {
      const msg = (await res.json().catch(() => ({}))).error || "Export failed";
      alert(msg);
      return;
    }

    const blob = await res.blob();
    downloadBlob(blob, `${title}.pdf`);
  } catch (err) {
    console.error(err);
    alert("Could not reach the export service.");
  } finally {
    setBusy(false);
  }
}

function downloadBlob(blob, filename) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
}

function downloadMarkdown() {
  const title = titleInput.value.trim() || "document";
  const blob = new Blob([editor.value], { type: "text/markdown" });
  downloadBlob(blob, `${title}.md`);
}

async function exportHtml() {
  const title = titleInput.value.trim() || "document";
  const payload = { markdown: editor.value, title };
  setBusy(true);
  try {
    const res = await fetch("/render-html", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!res.ok) {
      const msg = (await res.json().catch(() => ({}))).error || "Export failed";
      alert(msg);
      return;
    }

    const data = await res.json();
    const newWindow = window.open();
    if (newWindow) {
      newWindow.document.write(data.html);
      newWindow.document.close();
    } else {
      alert("Please allow pop-ups to view HTML output.");
    }
  } catch (err) {
    console.error(err);
    alert("Could not render HTML.");
  } finally {
    setBusy(false);
  }
}

function toggleLayout() {
  const focus = workspace.classList.contains("focus");
  if (focus) {
    workspace.classList.remove("focus");
    workspace.classList.add("split");
    toggleLayoutBtn.textContent = "Split View";
  } else {
    workspace.classList.remove("split");
    workspace.classList.add("focus");
    toggleLayoutBtn.textContent = "Focus Mode";
  }
}

function setBusy(state) {
  [savePdfBtn, exportBtn, saveMdBtn, exportHtmlBtn].forEach((btn) => {
    btn.disabled = state;
    btn.style.opacity = state ? 0.6 : 1;
  });
}

function bindMenu() {
  const actions = {
    new: () => {
      if (editor.value.trim() && !confirm("Start a new document? This will clear your current work.")) {
        return;
      }
      editor.value = "";
      titleInput.value = "Untitled document";
      localStorage.removeItem(STORAGE_KEY);
      localStorage.removeItem(TITLE_KEY);
      renderPreview();
    },
    edit: () => editor.focus(),
    view: () => toggleLayout(),
    html: () => exportHtml(),
    help: () => {
      const message = `PYMARK - MARKDOWN TO PDF CONVERTER

📐 MATHEMATICAL EQUATIONS:
✓ Inline math: \\\\(E = mc^2\\\\) (use \\\\(...\\\\) delimiters)
✓ Display math: $$\\\\\\\\int f(x)dx$$ (use double $$ delimiters)
✓ Subscripts: \\\\(x_i, y_{ij}\\\\) use _ or _{...}
✓ Superscripts: \\\\(x^2, e^{2x}\\\\) use ^ or ^{...}
✓ Full KaTeX support in preview

💵 CURRENCY vs MATH:
• Dollar signs for prices: $100, $50 (displays as-is)
• Math equations: Use \\\\(...\\\\) to avoid conflicts
  Example: \\\\(\\\\alpha_{0} = 0.5\\\\)

⚠️ PDF EXPORT WITH MATH:
• "Export PDF" button shows LaTeX source (limitation)
• For rendered equations in PDF:
  1. Click "Open HTML" in menu
  2. Use browser Print → Save as PDF (⌘+P / Ctrl+P)
  3. Get perfect math rendering!

✨ FEATURES:
• Auto-save to browser
• Import from file/URL
• Live preview
• Split/focus modes

📚 Learn Markdown: markdownguide.org
📐 LaTeX Math Reference: katex.org/docs/supported.html`;
      alert(message);
    },
  };

  menuItems.forEach((item) => {
    item.addEventListener("click", () => {
      const action = item.dataset.action;
      if (action && actions[action]) actions[action]();
    });
  });
}

function bindImports() {
  uploadBtn.addEventListener("click", () => fileInput.click());

  fileInput.addEventListener("change", () => {
    const file = fileInput.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (evt) => {
      const text = evt.target?.result || "";
      editor.value = typeof text === "string" ? text : "";
      renderPreview();
      persistDraft();
    };
    reader.readAsText(file);
    fileInput.value = ""; // reset
  });

  urlBtn.addEventListener("click", async () => {
    const url = urlInput.value.trim();
    if (!url) {
      alert("Please enter a URL to load.");
      return;
    }

    setBusy(true);
    try {
      const res = await fetch("/fetch-url", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });

      if (!res.ok) {
        const msg = (await res.json().catch(() => ({}))).error || "Could not load URL";
        alert(msg);
        return;
      }

      const data = await res.json();
      editor.value = data.markdown || "";
      renderPreview();
      persistDraft();
    } catch (err) {
      console.error(err);
      alert("Failed to fetch the URL.");
    } finally {
      setBusy(false);
    }
  });
}

function syncScroll(source, target) {
  if (isSyncScrolling) return;
  isSyncScrolling = true;
  
  // Calculate scroll percentage of source
  const scrollPercentage = source.scrollTop / (source.scrollHeight - source.clientHeight);
  
  // Apply same percentage to target
  target.scrollTop = scrollPercentage * (target.scrollHeight - target.clientHeight);
  
  // Reset flag after a short delay
  setTimeout(() => {
    isSyncScrolling = false;
  }, 50);
}

function init() {
  loadDraft();
  renderPreview();
  bindMenu();
  bindImports();

  editor.addEventListener("input", () => {
    renderPreview();
    persistDraft();
  });

  // Synchronized scrolling: editor -> preview
  editor.addEventListener("scroll", () => {
    syncScroll(editor, preview);
  });

  // Synchronized scrolling: preview -> editor
  preview.addEventListener("scroll", () => {
    syncScroll(preview, editor);
  });

  titleInput.addEventListener("input", persistDraft);
  toggleLayoutBtn.addEventListener("click", toggleLayout);
  saveMdBtn.addEventListener("click", downloadMarkdown);
  exportHtmlBtn.addEventListener("click", exportHtml);
  savePdfBtn.addEventListener("click", exportPdf);
  exportBtn.addEventListener("click", exportPdf);
}

init();
