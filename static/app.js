const editor = document.getElementById("editor");
const preview = document.getElementById("preview");
const titleInput = document.getElementById("doc-title");
const workspace = document.getElementById("workspace");
const toggleLayoutBtn = document.getElementById("toggle-layout");
const saveMdBtn = document.getElementById("save-md");
const savePdfBtn = document.getElementById("save-pdf");
const exportBtn = document.getElementById("export-btn");
const charCount = document.getElementById("char-count");
const wordCount = document.getElementById("word-count");
const menuItems = document.querySelectorAll(".menu-item");
const uploadBtn = document.getElementById("upload-btn");
const fileInput = document.getElementById("file-input");
const urlInput = document.getElementById("url-input");
const urlBtn = document.getElementById("url-btn");

const STORAGE_KEY = "md_to_pdf_draft";
const TITLE_KEY = "md_to_pdf_title";

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
  const html = marked.parse(raw);
  preview.innerHTML = DOMPurify.sanitize(html, { USE_PROFILES: { html: true } });
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
  [savePdfBtn, exportBtn, saveMdBtn].forEach((btn) => {
    btn.disabled = state;
    btn.style.opacity = state ? 0.6 : 1;
  });
}

function bindMenu() {
  const actions = {
    new: () => {
      if (editor.value.trim() && !confirm("Start a new document? Unsaved changes will be kept in downloads only.")) {
        return;
      }
      editor.value = "";
      titleInput.value = "Untitled document";
      renderPreview();
    },
    edit: () => editor.focus(),
    view: () => toggleLayout(),
    help: () => window.open("https://www.markdownguide.org/", "_blank"),
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

function init() {
  loadDraft();
  renderPreview();
  bindMenu();
  bindImports();

  editor.addEventListener("input", () => {
    renderPreview();
    persistDraft();
  });

  titleInput.addEventListener("input", persistDraft);
  toggleLayoutBtn.addEventListener("click", toggleLayout);
  saveMdBtn.addEventListener("click", downloadMarkdown);
  savePdfBtn.addEventListener("click", exportPdf);
  exportBtn.addEventListener("click", exportPdf);
}

init();
