#!/usr/bin/env python3
"""Comprehensive fix for all mathematical notation in Study Plan.md"""

# Read the file
with open('Study Plan.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Process each line
output_lines = []
i = 0

while i < len(lines):
    line = lines[i]
    
    # Fix the main mathematical formulation section (lines around 355-375)
    if "For a given ROI time series" in line and "S(t)" in line:
        # Replace this section with properly formatted math
        output_lines.append("For a given ROI time series $S(t)$ over a trial ($t \\in \\{t_0, t_1, ..., t_L\\}$):\n")
        i += 1
        continue
    
    if line.strip().startswith("1. **Identify minimum:**") and "t_m" in line:
        output_lines.append("1. **Identify minimum:** Determine time $t_m$ when signal is minimized (start of task-related activation).\n")
        i += 1
        continue
    
    if line.strip().startswith("2. **Set baseline:**") and "B(t_m)" in line:
        output_lines.append("2. **Set baseline:** $B(t_m) = S(t_m)$ (initialize baseline to minimum).\n")
        i += 1
        continue
    
    if "**Iterate through timepoints**" in line:
        output_lines.append("3. **Iterate through timepoints** $t \\in \\{t_m, t_m+1, ..., t_L\\}$:\n")
        i += 1
        continue
    
    if "If S(t_{i+1}) > B(t_i)" in line:
        output_lines.append("   - If $S(t_{i+1}) > B(t_i)$: **generate a spike** at time $t_{i+1}$, and update baseline as:\n")
        i += 1
        # Skip the next line if it's just a dash
        if i < len(lines) and lines[i].strip() in ['-', '- ']:
            i += 1
        # Check if next line has the equation
        if i < len(lines) and '$$' in lines[i]:
            # Found display math, keep it but fix the content
            i += 1  # Skip $$
            if i < len(lines):
                eq_line = lines[i].strip()
                # Clean up the equation
                eq_line = eq_line.replace('\\\\alpha', '\\alpha').replace('\\\\cdot', '\\cdot')
                output_lines.append("\n$$\n")
                output_lines.append(eq_line + "\n")
                output_lines.append("$$\n")
                i += 1
                if i < len(lines) and '$$' in lines[i]:
                    i += 1  # Skip closing $$
        continue
    
    if "If S(t_{i+1})" in line and "leq" in line:
        output_lines.append("   - If $S(t_{i+1}) \\leq B(t_i)$: **no spike**, and reset baseline as:\n")
        i += 1
        # Next line might have the equation
        if i < len(lines) and "B(t_{i+1}) = S(t_{i+1})" in lines[i]:
            output_lines.append("\n$$\n")
            output_lines.append("B(t_{i+1}) = S(t_{i+1})\n")
            output_lines.append("$$\n")
            i += 1
        continue
    
    if "Where **" in line and "alpha" in line and "[0, 1]" in line:
        output_lines.append("Where $\\alpha \\in [0, 1]$ is a parameter controlling how quickly the baseline adapts to signal increases. Typical value: $\\alpha = 0.5$ (Kasabov et al. 2017).\n")
        i += 1
        continue
    
    # Fix other alpha references
    if "**α" in line or "**\\\\alpha" in line:
        line = line.replace("**α", "$\\alpha$").replace("**\\\\alpha", "$\\alpha$")
    if "α =" in line or "\\\\alpha =" in line:
        line = line.replace("α =", "$\\alpha =$").replace("\\\\alpha =", "$\\alpha =$")
    if "α ∈" in line or "α \\in" in line or "\\\\alpha \\in" in line:
        line = line.replace("α ∈", "$\\alpha \\in$").replace("α \\in", "$\\alpha \\in$").replace("\\\\alpha \\in", "$\\alpha \\in$")
    
    # Fix >= symbols
    line = line.replace(" \\geq ", " $\\geq$ ")
    line = line.replace("≥", "$\\geq$")
    
    # Fix approximately symbols  
    line = line.replace(" \\approx ", " $\\approx$ ")
    
    # Fix times symbol
    line = line.replace(" \\times ", " $\\times$ ")
    
    # Fix double backslashes
    line = line.replace("\\\\alpha", "\\alpha")
    line = line.replace("\\\\cdot", "\\cdot")
    line = line.replace("\\\\in", "\\in")
    line = line.replace("\\\\geq", "\\geq")
    line = line.replace("\\\\leq", "\\leq")
    line = line.replace("\\\\approx", "\\approx")
    line = line.replace("\\\\times", "\\times")
    
    output_lines.append(line)
    i += 1

# Write back
with open('Study Plan.md', 'w', encoding='utf-8') as f:
    f.writelines(output_lines)

print("Comprehensive math fix completed!")
