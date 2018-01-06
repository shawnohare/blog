---
date: 2017-11-25T11:15:01
description: Showcase some mathematics in markdown.
markup: mmark 
math: true

slug: AE8073E5-FAAD-4768-AA20-153731F16DE6
subtitle: Rendering mathematics for the web
tags:
- latex
- mathjax
- markdown
- commonmark
- hugo
title: Math (LaTeX) in Markdown

---

# Introduction

When writing mathematics in markdown, I prefer a combination of syntactically
pure but robust LaTeX, portability with respect to markdown processors, and
aesthetically pleasing in-editor highlighting. Unfortunately, the first two
constraints often conflict.

<!--more-->

With the exception of [`pandoc`](https://pandoc.org), most markdown processors
do not cater to highly mathematical documents. In particular, they tend to
render `$` rather than treat it as a math delimiter or will inadvertently
process raw LaTeX, requiring excessive escapes for common LaTeX syntax such as
the set delimiter `\{`.  That there is no canonical math delimiter in the
markdown specification is a gross oversight in the standard, but that's a topic
in its own right. (Hopefully the work at [CommonMark](http://commonmark.org)
will lead to satisfactory math extension).

As it currently stands, those wishing to inject LaTeX into their markdown are
subject to unfortunate contortions. Confer
[math in markdown](https://github.com/cben/mathdown/wiki/math-in-markdown).

# MathJax

[MathJax](https://mathjax.org) is a JavaScript display engine for rendering
mathematics in web browsers. It supports relatiely sophisticated
LaTeX, such as `align` environments and equation references. I currently
use it to render all mathematics on this site.

The following MathJax config is included in the `<head>` of each page
containing LaTeX. 

```html
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    displayMath: [['$$','$$'], ['\\[','\\]']],
    processEscapes: true,
    processEnvironments: true,
    processRefs: true,
    menuSettings: { zoom: "Double-Click" },
    processClass: "math",
    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
  },
  TeX: {
    equationNumbers: { autoNumber: "AMS" },
    extensions: ["AMSmath.js", "AMSsymbols.js"],
  },
});
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_HTML-full">
</script>
```

# kramdown, mmark, and the `$$` delimiter 


The `kramdown` markdown processor (and its derivatives such as `mmark`)
utilize `$$` as the singular delimiter for mathematics, both inline and display.
Since no further processing occurs inside the `$$` delimiters, one is free to
write essentially pure latex. 

The inline expression 
$$2 := \{0, 1\} = \{\emptyset, \{\emptyset \}\}$$ is rendered from:

```latex
$$2 := \{0, 1\} = \{\emptyset, \{\emptyset \}\}$$
```

For display mathematics, I prefer to use explicit environments, which must
themselves be wrapped in `$$` tags.

$$\begin{equation*}
\mathfrak C_n := \left\{ \xi^0, \xi^1, \xi^2, \dots, \xi^{n-1} \right\}
\end{equation*}$$

is rendered from :

```
$$\begin{equation*}
\mathfrak C_n := \left\{ \xi^0, \xi^1, \xi^2, \dots, \xi^{n-1} \right\}
\end{equation*}$$
```

The advantage with this approach is that `$$...$$` and
`$$\begin{*}...\end{*}$$` always delimit inline and display mathematics,
respectively. This simplifies source transformation.


# hugo

Presently I employ `hugo` to generate this site from markdown content. One
nice feature of `hugo` is that it supports `mmark` automatically by
either utilizing the `.mmark` file extension or explicitly specifying `mmark`
as the processor in the page metadata. For example, this page's metadata is:

```yaml
---
date: "2017-11-25"
title:  "Mathematics (LaTeX) in Markdown"
description: "Showcase some mathematics in markdown."
math:  true
tags:  ["latex", "mathjax", "markdown", "commonmark", "hugo"]
markup:  "mmark"

---
```


# Showcase

Some mathematical expressions:

$$\begin{equation*}
\mathfrak G \mathrel{\vcenter{:}}= \coprod_{i=1}^{\infty} \widehat{\mathbb X}_{\{ j \lt i \}}
\end{equation*}$$

$$\begin{equation*}
\left( \sum_{k=1}^n a_k b_k \right)^{2} \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right) 
\end{equation*}$$

$$\begin{equation*}
 \mathbf{V}_1 \times \mathbf{V}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \newline \frac{\partial X}{\partial u} & \frac{\partial Y}{\partial u} & 0 \newline \frac{\partial X}{\partial v} & \frac{\partial Y}{\partial v} & 0 \newline \end{vmatrix}
\end{equation*}$$

$$\begin{equation*}
\frac{1}{(\sqrt{\phi \sqrt{5}}-\phi) e^{\frac25 \pi}} = 1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}} {1+\frac{e^{-8\pi}} {1+\ldots} } } }
\end{equation*}$$

$$\begin{equation*}
1 + \frac{q^2}{(1-q)}+\frac{q^6}{(1-q)(1-q^2)}+\cdots = \prod_{j=0}^{\infty}\frac{1}{(1-q^{5j+2})(1-q^{5j+3})}, \quad\quad \text{for $|q| \lt 1$}.
\end{equation*}$$

$$\begin{align} 
\nabla \times \vec{\mathbf{B}} -, \frac1c, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \newline \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \newline \nabla \times \vec{\mathbf{E}}, +, \frac1c, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \newline \nabla \cdot \vec{\mathbf{B}} & = 0
\end{align}$$

$$\begin{equation} \label{eq:showcase}
x(t) = e^{\int_{t_0}^tp(s)ds}\Bigg(\int_{t_0}^t\Big(q(s)e^{-\int_{t_0}^sp(\tau)d\tau}\Big)ds + x_0\Bigg). 
\end{equation}$$

We can even reference equation $$\eqref{eq:showcase}$$.
