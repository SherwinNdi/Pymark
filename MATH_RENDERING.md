# Mathematical Equation Rendering in Pymark

## Current Implementation

### ✅ Web Preview (Fully Working)
The web interface uses **KaTeX 0.16.9** for real-time mathematical equation rendering.

**Supported LaTeX delimiters:**
- Inline math: `\(...\)` (recommended) or `$...$`
- Display math: `$$...$$` or `\[...\]`

**Important:** Use `\(...\)` for inline math to avoid conflicts with currency symbols ($100, $50, etc.)

**Example:**
```markdown
Price: $100 (regular dollar sign - displays as-is)

Einstein's equation: \(E = mc^2\) (inline math with \(...\))

Quadratic formula:
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
```

### ⚠️ PDF Export (Limitation)

**Current behavior:** PDF export uses WeasyPrint, which does NOT support JavaScript. This means:
- LaTeX source code appears in PDFs (e.g., `$E = mc^2$`)
- Math is NOT rendered as formatted equations

**Why?** WeasyPrint is a CSS-based PDF renderer that doesn't execute JavaScript, so KaTeX cannot run.

## Solutions for PDF Math Rendering

### Option 1: Use HTML Export (Recommended for now)
1. Click **"Open HTML"** in the menu
2. The HTML opens in a new tab with fully rendered math (KaTeX)
3. Use your browser's Print → Save as PDF
4. Result: PDF with properly rendered equations

**Advantages:**
- ✅ Works immediately
- ✅ Perfect math rendering
- ✅ No additional dependencies

**Disadvantages:**
- ❌ Manual two-step process

### Option 2: Pre-process LaTeX to Images (Future Enhancement)

Install additional dependencies:
```bash
pip install latex2image pillow
```

This would convert each LaTeX expression to an embedded image before PDF generation.

**Advantages:**
- ✅ Automatic PDF generation with math
- ✅ Works with WeasyPrint

**Disadvantages:**
- ❌ Requires LaTeX installation on system
- ❌ Larger PDF file sizes
- ❌ Images may not scale well

### Option 3: Headless Browser Rendering (Best Quality)

Install Playwright or Selenium:
```bash
pip install playwright
playwright install chromium
```

Replace WeasyPrint with browser-based PDF generation.

**Advantages:**
- ✅ Perfect rendering (uses real browser)
- ✅ JavaScript support (KaTeX works)
- ✅ Professional output

**Disadvantages:**
- ❌ Slower generation
- ❌ Larger dependency (~300MB for browser)
- ❌ More complex setup

### Option 4: Server-side LaTeX Compilation

Use **pandoc** with LaTeX:
```bash
brew install pandoc
brew install --cask basictex  # or full MacTeX
```

**Advantages:**
- ✅ Publication-quality typesetting
- ✅ Widely used in academia

**Disadvantages:**
- ❌ Large installation (~4GB for MacTeX)
- ❌ Different rendering than preview
- ❌ More complex configuration

## Recommended Workflow

**For immediate use:**
1. Edit and preview in Pymark (math renders perfectly)
2. Export as HTML
3. Print to PDF from browser

**For production deployment:**
Implement Option 3 (Playwright) for automated high-quality PDF generation.

## Testing Math Rendering

Use the included `math_renderer.py` utility to:
- Extract and validate LaTeX expressions
- Check for delimiter mismatches
- Convert to Unicode (fallback display)

```bash
python math_renderer.py
```

## Common LaTeX Syntax

| Element | Inline | Display |
|---------|--------|---------|
| Fractions | `$\frac{a}{b}$` | `$$\frac{a}{b}$$` |
| Superscript | `$x^2$` | `$$x^2$$` |
| Subscript | `$x_i$` | `$$x_i$$` |
| Greek letters | `$\alpha, \beta, \gamma$` | - |
| Integrals | `$\int_a^b f(x)dx$` | `$$\int_a^b f(x)dx$$` |
| Summation | `$\sum_{i=1}^n x_i$` | `$$\sum_{i=1}^n x_i$$` |
| Matrices | - | `$$\begin{bmatrix}a&b\\c&d\end{bmatrix}$$` |

## Browser Compatibility

KaTeX rendering requires modern browsers:
- ✅ Chrome/Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+

## Troubleshooting

**Math not rendering in preview:**
1. Check browser console for errors (F12)
2. Verify KaTeX loaded: Open DevTools → Network tab
3. Validate LaTeX syntax: `python math_renderer.py`

**Unmatched delimiters:**
- Every `$` needs a closing `$`
- Every `$$` needs a closing `$$`
- Use `\$` to display a literal dollar sign

**PDF shows LaTeX source:**
- This is expected with current WeasyPrint backend
- Use HTML export → Print to PDF workflow
- Or wait for browser-based PDF rendering feature

## Future Enhancements

Priority list for math rendering improvements:
1. ✅ KaTeX integration in web preview (DONE)
2. ⏳ Playwright/Selenium PDF generation (TODO)
3. ⏳ Math syntax validator in editor (TODO)
4. ⏳ Live LaTeX error highlighting (TODO)
5. ⏳ Math equation library/snippets (TODO)
