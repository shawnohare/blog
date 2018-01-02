---
title: "sample title"
description: "sample desc"
date: "2017-11-30"
draft: true
math: true
toc:  true
categories:  ["x", "y"]
groups:  ["x", "y"]
tags:  ["x", "y"]
series: ["x"]
markup: "pandoc"

---

Some inline math $\{ \xi_2^3 \}$ and display:

\begin{equation}
\sum_{i=1}^{\infty} \int_{x = a_i}^{b_i} f_i(x) \ dx
\end{equation}

Some inline `code \{ \}` and some block code:
```python
def f(x: str) -> str:
    return x[1:]
```

# Header with some `code \{...\}` and $\LaTeX$

<!--more-->
