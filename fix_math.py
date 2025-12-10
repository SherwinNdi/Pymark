#!/usr/bin/env python3
"""Fix mathematical notation in Study Plan.md"""

import re

# Read the file
with open('Study Plan.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace special characters with LaTeX equivalents
replacements = [
    ('·', r' \\cdot '),
    ('â‰¥', r' \\geq '),
    ('â‰ˆ', r' \\approx '),
    ('≤', r' \\leq '),
    ('â‚€', '_0'),
    ('â‚', '_1'),
    ('â‚‚', '_2'),
    ('Ã—', r' \\times '),
    ('∈', r' \\in '),
    ('→', r' \\to '),
    ('α', r'\\alpha'),
]

for old, new in replacements:
    content = content.replace(old, new)

# Now wrap specific mathematical expressions in $ or $$
# Pattern 1: Wrap inline math like "S(t_{i+1})"
inline_patterns = [
    (r'(\b[A-Z]\([a-z_0-9{}]+\))', r'$\1$'),  # S(t_i), B(t_m), etc.
    (r'(\balpha\b)', r'$\\alpha$'),  # alpha
    (r'(\bt_\{[im0-9]+\})', r'$\1$'),  # t_{i+1}, t_m, t_0
    (r'(\bt_[iml])', r'$\1$'),  # t_i, t_m, t_l
]

# Pattern 2: Identify equations that should be display math ($$)
# Look for lines with = that aren't already in $$
lines = content.split('\n')
new_lines = []

for i, line in enumerate(lines):
    # Skip if already has LaTeX delimiters
    if '$$' in line or (line.strip().startswith('$') and line.strip().endswith('$')):
        new_lines.append(line)
        continue
    
    # Check if this is an equation line (starts with spaces/tabs and has =)
    stripped = line.strip()
    if stripped.startswith('- ') and '=' in stripped and '\\' in stripped:
        # This looks like an equation in a list
        # Extract the equation part
        eq_match = re.search(r'(B\([^)]+\)\s*=.+)', stripped)
        if eq_match:
            eq = eq_match.group(1)
            # Wrap in display math
            prefix = stripped[:stripped.index(eq)]
            new_line = '     ' + prefix + '\n\n$$\n' + eq + '\n$$\n'
            new_lines.append(new_line)
            continue
    
    new_lines.append(line)

content = '\n'.join(new_lines)

# Write back
with open('Study Plan.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed mathematical notation in Study Plan.md")
