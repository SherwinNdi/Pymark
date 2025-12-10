#!/usr/bin/env python3
"""
Final comprehensive fix for mathematical notation in Study Plan.md
"""

import re

def fix_mathematical_notation(text):
    """Apply all mathematical notation fixes."""
    
    # Step 1: Fix encoding artifacts with direct string replacement
    text = text.replace('Î \\cdot Â²', '$\\eta^2$')
    text = text.replace('Ï‡Â²', '$\\chi^2$')
    text = text.replace('ΔRÂ²', '$\\Delta R^2$')
    text = text.replace('âœ"', '✓')
    text = text.replace('Â·', '$\\cdot$')
    
    # Step 2: Fix sample sizes (n = X)
    text = re.sub(r'\bn = (\d+[-–\d]*)\b', r'$n = \1$', text)
    
    # Step 3: Fix time expressions
    text = re.sub(r'(?<![=:])\bt = (\d+[-–\d]*\.?\d* ?s?)\b', r'$t = \1$', text)
    
    # Step 4: Fix coordinates
    text = re.sub(r'\b([xyz])=([±\d\.]+)', r'$\1=\2$', text)
    
    # Step 5: Fix ΔRT and RT variables (not already in math mode or backticks)
    text = re.sub(r'(?<![`$])ΔRT(_\w+)?(?![`$])', lambda m: f'${m.group(0)}$', text)
    text = re.sub(r'(?<![`$_:])\bRT(_\w+)?(?![`$\w])(?=[\s,\.\)])', lambda m: f'${m.group(0)}$', text)
    
    # Step 6: Fix statistical expressions
    text = re.sub(r'(?<![`$])\br ([<>=]) ([-\d\.]+)(?![`$])', r'$r \1 \2$', text)
    text = re.sub(r'(?<![`$])\bp ([<>=]) ([\d\.]+)(?![`$])', r'$p \1 \2$', text)
    text = re.sub(r'(?<![`$])\bd = ([\d\.]+)(?![`$])', r'$d = \1$', text)
    text = re.sub(r'(?<![`$])\bt\((\d+)\) = ([-\dX\.]+)(?![`$])', r'$t(\1) = \2$', text)
    text = re.sub(r'(?<![`$])\bF\((\d+),(\d+)\) = ([-\dX\.]+)(?![`$])', r'$F(\1,\2) = \3$', text)
    
    # Step 7: Fix specific formulas
    text = text.replace('PES = RT_after_error - RT_baseline', 
                       '$\\text{PES} = \\text{RT}_{\\text{after error}} - \\text{RT}_{\\text{baseline}}$')
    text = text.replace('ΔRT_reward = RT_neutral - RT_reward',
                       '$\\Delta\\text{RT}_{\\text{reward}} = \\text{RT}_{\\text{neutral}} - \\text{RT}_{\\text{reward}}$')
    
    # Step 8: Fix Greek letters (not in math mode or after backslash)
    greek_letters = ['alpha', 'beta', 'chi', 'delta', 'Delta', 'eta', 'gamma']
    for letter in greek_letters:
        # Don't replace if already in math mode or preceded by backslash
        pattern = r'(?<![`$\\])\b' + letter + r'\b(?![`$])'
        replacement = '$\\\\' + letter + '$'  # Need to double escape for literal backslash
        text = re.sub(pattern, replacement, text)
    
    # Step 9: Fix arrows in context
    text = re.sub(r'(?<![`$])(Reward|reward) \\to (Control|control)(?![`$])', 
                 r'$\1 \\to \2$', text)
    
    return text

def main():
    input_file = '/Users/nedaeija/Documents/Devs/md_to_pdf/Study Plan.md'
    
    # Read file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply fixes
    fixed_content = fix_mathematical_notation(content)
    
    # Write back
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("✓ Final mathematical notation fixes applied successfully!")
    print("All encoding artifacts cleaned and LaTeX formatting applied.")

if __name__ == '__main__':
    main()
