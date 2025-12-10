"""
Mathematical equation rendering utilities for Pymark.
Provides LaTeX math rendering support for both web preview and PDF export.
"""

import re
from typing import List, Tuple


def extract_math_expressions(text: str) -> List[Tuple[str, str, bool]]:
    """
    Extract LaTeX math expressions from markdown text.
    
    Returns:
        List of tuples: (original, latex_content, is_display)
        where is_display=True for display math ($$...$$), False for inline ($...$)
    """
    expressions = []
    
    # Display math ($$...$$)
    display_pattern = r'\$\$(.*?)\$\$'
    for match in re.finditer(display_pattern, text, re.DOTALL):
        expressions.append((match.group(0), match.group(1).strip(), True))
    
    # Inline math ($...$) - but not $$
    inline_pattern = r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)'
    for match in re.finditer(inline_pattern, text):
        expressions.append((match.group(0), match.group(1).strip(), False))
    
    return expressions


def convert_latex_to_unicode(latex: str) -> str:
    """
    Convert simple LaTeX expressions to Unicode for plain text display.
    This is a fallback for environments without proper math rendering.
    """
    replacements = {
        r'\alpha': 'α',
        r'\beta': 'β',
        r'\gamma': 'γ',
        r'\delta': 'δ',
        r'\Delta': 'Δ',
        r'\epsilon': 'ε',
        r'\eta': 'η',
        r'\theta': 'θ',
        r'\lambda': 'λ',
        r'\mu': 'μ',
        r'\pi': 'π',
        r'\rho': 'ρ',
        r'\sigma': 'σ',
        r'\tau': 'τ',
        r'\phi': 'φ',
        r'\chi': 'χ',
        r'\omega': 'ω',
        r'\geq': '≥',
        r'\leq': '≤',
        r'\neq': '≠',
        r'\approx': '≈',
        r'\pm': '±',
        r'\times': '×',
        r'\div': '÷',
        r'\cdot': '·',
        r'\to': '→',
        r'\rightarrow': '→',
        r'\leftarrow': '←',
        r'\in': '∈',
        r'\subset': '⊂',
        r'\subseteq': '⊆',
        r'\cup': '∪',
        r'\cap': '∩',
        r'\infty': '∞',
        r'\partial': '∂',
        r'\nabla': '∇',
        r'\int': '∫',
        r'\sum': '∑',
        r'\prod': '∏',
    }
    
    result = latex
    for latex_cmd, unicode_char in replacements.items():
        result = result.replace(latex_cmd, unicode_char)
    
    # Handle subscripts and superscripts (simplified)
    result = re.sub(r'_\{([^}]+)\}', r'_\1', result)
    result = re.sub(r'\^\{([^}]+)\}', r'^\1', result)
    
    # Clean up remaining LaTeX commands
    result = re.sub(r'\\text\{([^}]+)\}', r'\1', result)
    result = result.replace('{', '').replace('}', '')
    
    return result


def enhance_markdown_with_math_hints(markdown_text: str) -> str:
    """
    Add HTML comments to help identify math regions for PDF processors.
    This can help external tools understand where math is located.
    """
    # Add markers around display math
    markdown_text = re.sub(
        r'\$\$(.*?)\$\$',
        r'<!-- MATH:DISPLAY:START -->\n$$\1$$\n<!-- MATH:DISPLAY:END -->',
        markdown_text,
        flags=re.DOTALL
    )
    
    # Add markers around inline math
    markdown_text = re.sub(
        r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)',
        r'<!-- MATH:INLINE:START -->$\1$<!-- MATH:INLINE:END -->',
        markdown_text
    )
    
    return markdown_text


def validate_latex_delimiters(text: str) -> List[str]:
    """
    Check for common LaTeX delimiter issues.
    
    Returns:
        List of warning messages about potential issues.
    """
    warnings = []
    
    # Check for unmatched dollar signs
    single_dollars = re.findall(r'(?<!\$)\$(?!\$)', text)
    if len(single_dollars) % 2 != 0:
        warnings.append("Unmatched single $ delimiters detected - math may not render correctly")
    
    # Check for unmatched double dollars
    double_dollars = re.findall(r'\$\$', text)
    if len(double_dollars) % 2 != 0:
        warnings.append("Unmatched $$ delimiters detected - display math may not render correctly")
    
    # Check for common LaTeX command typos
    if re.search(r'\\[a-zA-Z]+(?![a-zA-Z{])', text):
        warnings.append("Possible incomplete LaTeX commands detected")
    
    return warnings


if __name__ == "__main__":
    # Test the utilities
    sample = """
    This is inline math: $\\alpha + \\beta = \\gamma$
    
    And display math:
    $$
    E = mc^2
    $$
    
    More complex: $f(x) = \\int_{-\\infty}^{\\infty} e^{-x^2} dx$
    """
    
    expressions = extract_math_expressions(sample)
    print(f"Found {len(expressions)} math expressions:")
    for orig, latex, is_display in expressions:
        mode = "display" if is_display else "inline"
        print(f"  [{mode}] {latex}")
        print(f"    Unicode: {convert_latex_to_unicode(latex)}")
    
    warnings = validate_latex_delimiters(sample)
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")
    else:
        print("\n✓ No LaTeX delimiter issues detected")
