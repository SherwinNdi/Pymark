# Math Syntax Quick Reference

## Testing Inline Math

This costs $100 and that costs $50. (regular currency)

Now math: \(E = mc^2\) and \(a^2 + b^2 = c^2\)

## Subscripts

**Basic subscript:** \(x_i\) where i is the index

**Multiple characters:** \(x_{ij}\) or \(a_{max}\) 

**Nested:** \(x_{i_j}\) (subscript of subscript)

**Examples:**
- Array element: \(a_1, a_2, ..., a_n\)
- Matrix: \(A_{ij}\) where \(i, j \in \{1, 2, 3\}\)
- Time series: \(y_t, y_{t-1}, y_{t+1}\)
- Statistical: \(\bar{x}_n, s^2_n\)

## Superscripts

**Basic power:** \(x^2\) or \(e^x\)

**Multiple characters:** \(e^{2x}\) or \(x^{10}\)

**Combining:** \(x_i^2\) or \(e^{-x^2}\)

**Examples:**
- Powers: \(2^8 = 256\)
- Exponentials: \(e^{i\pi} = -1\)
- Derivatives: \(f'(x)\) or \(f^{(n)}(x)\)

## Display Math with Subscripts/Superscripts

Summation:
$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$

Integration:
$$
\int_{a}^{b} f(x)dx
$$

Product:
$$
\prod_{i=1}^{n} a_i
$$

Matrix notation:
$$
A_{m \times n} = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

## Statistical Formulas

Sample mean:
$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

Variance:
$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2
$$

Linear regression:
$$
\hat{y}_i = \beta_0 + \beta_1 x_i + \epsilon_i
$$

## Common Mistakes

❌ Wrong: \(x_ij\) renders as \(x_i j\) - missing braces!

✅ Correct: \(x_{ij}\) - use braces for multiple characters

❌ Wrong: \(e^2x\) renders as \(e^2 x\) - only first character is superscript

✅ Correct: \(e^{2x}\) - use braces for entire expression

## Complex Examples

Inline complex: The formula \(f(x) = \sum_{i=0}^{n} a_i x^i\) is a polynomial.

Display complex:
$$
\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(x_1, ..., x_i + h, ..., x_n) - f(x_1, ..., x_i, ..., x_n)}{h}
$$

Neural network weights:
$$
w_{ij}^{(l)} \leftarrow w_{ij}^{(l)} - \alpha \frac{\partial L}{\partial w_{ij}^{(l)}}
$$

## Quick Syntax Table

| What | LaTeX | Result |
|------|-------|--------|
| Subscript | `x_i` | \(x_i\) |
| Multi-char subscript | `x_{ij}` | \(x_{ij}\) |
| Superscript | `x^2` | \(x^2\) |
| Multi-char superscript | `e^{2x}` | \(e^{2x}\) |
| Both | `x_i^2` | \(x_i^2\) |
| Nested subscript | `x_{i_j}` | \(x_{i_j}\) |
| Nested superscript | `x^{y^z}` | \(x^{y^z}\) |
| Greek with subscript | `\alpha_0` | \(\alpha_0\) |
| Greek with superscript | `\beta^*` | \(\beta^*\) |

## Tips

1. **Always use braces `{...}` for multi-character sub/superscripts**
2. **Test inline math:** Type `\(x_1\)` - should render as x with subscript 1
3. **Currency is safe:** Type `$100` - displays as regular text
4. **Check preview:** Math should render immediately after typing `\)`
