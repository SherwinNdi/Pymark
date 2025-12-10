# Mathematical Equations Demo

This document demonstrates Pymark's mathematical equation rendering using KaTeX.

## Currency vs Math

Regular prices work fine: The laptop costs $1,200 and the mouse costs $50.

You can mix currency and math in the same document without conflicts!

## Inline Math

Einstein's famous equation: \(E = mc^2\)

The Pythagorean theorem: \(a^2 + b^2 = c^2\)

Euler's identity: \(e^{i\pi} + 1 = 0\)

Greek letters: \(\alpha, \beta, \gamma, \delta, \theta, \lambda, \mu, \pi, \sigma, \omega\)

## Display Math

### Calculus

The fundamental theorem of calculus:

$$
\int_{a}^{b} f'(x)dx = f(b) - f(a)
$$

Gaussian integral:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

### Algebra

Quadratic formula:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

Binomial theorem:

$$
(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k
$$

### Linear Algebra

Matrix multiplication:

$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
ax + by \\
cx + dy
\end{bmatrix}
$$

### Statistics

Normal distribution:

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

Sample mean and variance:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i, \quad s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2
$$

### Physics

Schrödinger equation:

$$
i\hbar\frac{\partial}{\partial t}\Psi(r,t) = \hat{H}\Psi(r,t)
$$

Maxwell's equations:

$$
\begin{align}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_0} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0\mathbf{J} + \mu_0\epsilon_0\frac{\partial \mathbf{E}}{\partial t}
\end{align}
$$

## Complex Expressions

Inline fractions work too: \(\frac{dy}{dx} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}\)

Continued fractions:

$$
x = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \cdots}}}
$$

## Comparison Operators

Inequalities: \(a \leq b\), \(x \geq y\), \(m \neq n\), \(p \approx q\)

Set notation: \(x \in \mathbb{R}\), \(A \subseteq B\), \(C \cup D\), \(E \cap F\)

## Tips for PDF Export

**For mathematical equations in PDFs:**

1. Click **"Open HTML"** in the menu bar
2. The document opens in a new tab with fully rendered math
3. Use browser's Print function (⌘+P or Ctrl+P)
4. Select "Save as PDF"
5. Enjoy perfectly rendered equations!

**Note:** The direct "Export PDF" button uses WeasyPrint which doesn't support JavaScript/KaTeX, so it will show LaTeX source code instead of rendered equations.

---

*This document was created with Pymark - https://github.com/YourUsername/Pymark*
