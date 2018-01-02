+++
date = "2015-12-09"
updated = "2017-05-29"
title = "Feature Sandbox"
description="Showcase some of the site's features."
math = true
toc = true
tags = ["multi word tag", "sample", "latex", "mathjax"]
markup = "mmark"
+++

Herein we test how blog themes render particular content, especially
mathematics. 


<!--more-->

# Math

In an effort to avoid encountering Markdown processor nuances and
gotchas, I've decided to instruct Markdown processors to skip all
mathematical markup. A desirable side effect is that content can include
unadulterated LaTeX.

## Inline and Display

Very simple inline expressions can be included verbatim. For example 
`$\LaTeX$` renders to $\LaTeX$. More complicated inline expressions and
all display style mathematics should be included in `inline` and `display`
shortcodes, respectively. 

For example, {{< inline "$\sum_{n \in \mathbb{N}} \frac{1}{n^2}$" >}} 
is rendered from
`{{</* inline "$\sum_{n \in \mathbb{N}} \frac{1}{n^2}$" */>}}`

The tensor product construction for bisets induces a bilinear map
between Burnside rings via:
{{< display >}}
```
\[
  - \cdot_H - \colon B(G,H) \times B(H, K) \to B(G, K),
  \quad ([X], [Y]) \mapsto [X \times_H Y],
\]
```
{{< /display >}}
which is rendered from

    {{</* display */>}}
    \[
      - \cdot_H - \colon B(G,H) \times B(H, K) \to B(G, K),
      \quad ([X], [Y]) \mapsto [X \times_H Y],
    \]
    {{</* /display */>}}

These shortcode snippets inform the Markdown processor to ignore the content
and also trim the optional wrapping verbatim backticks. These backticks
can be included to avoid text editor highlighting issues.



# Introduction

When writing mathematics in markdown, I prefer a combination of syntactically
pure LaTeX, portability with respect to markdown processors, and aesthetically
pleasing in-editor highlighting. Unfortunately, the first two constraints often
conflict.

With the exception of `pandoc`, most markdown processors do not cater to highly
mathematical documents. In particular, they tend to render `$` rather than
treat it as a math delimiter or will inadvertently process raw LaTeX, requiring
excessive escapes for common LaTeX syntax such as the set delimiter `\{`.  That
there is no canonical math delimiter in the markdown specification is a gross
oversight in the standard, but that's a topic in its own right. (Hopefully the
work at [CommonMark](http://commonmark.org) will lead to satisfactory math
extension).

As it currently stands, those wishing to inject LaTeX into their markdown are
subject to unfortunate contortions. Confer
[math in markdown](https://github.com/cben/mathdown/wiki/math-in-markdown).


# kramdown, mmark, and the `$$` delimiter 

The `kramdown` markdown processor (and its derivatives such as `mmark`)
utilize `$$` as the singular delimiter for mathematics, both inline and display.
Since no further processing occurs inside the `$$` delimiters, one is free to
write essentially pure latex. For example the inline expression $$2 :=
\{0, 1\} = \{\emptyset, \{\emptyset \}\}$$ is rendered from:

```latex
$$2 := \{0, 1\} = \{\emptyset, \{\emptyset \}\}$$
```

For display mathematics, I prefer to use explicit environments wrapped
in `<pre>` tags, the contents of which most markdown processors skip. For
example,

<pre class="math">
\[
C_n := \left\{ \xi^0, \xi^1, \xi^2, \dots, \xi^{n-1} \right\}
\]
</pre>

is rendered from 

```
<pre class="math">
\[
C_n := \left\{ \xi^0, \xi^1, \xi^2, \dots, \xi^{n-1} \right\}
\]
</pre>
```

The advantage here is that `␣$$...$$␣` always denotes inline mathematics while

- `\n\n$$...$$\n\n` 
- `<pre class="math">...</pre>` 

always wrap display
blocks. This makes conversion to other formats less of a hassle.

# Showcase

<pre class="math">
\begin{equation*}
\left( \sum_{k=1}^n a_k b_k \right)^{2} \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right) 
\end{equation*}
</pre>

<pre class="math">
\begin{equation*}
 \mathbf{V}_1 \times \mathbf{V}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \newline \frac{\partial X}{\partial u} & \frac{\partial Y}{\partial u} & 0 \newline \frac{\partial X}{\partial v} & \frac{\partial Y}{\partial v} & 0 \newline \end{vmatrix}
\end{equation*}
</pre>

<pre class="math">
\begin{equation*}
\frac{1}{(\sqrt{\phi \sqrt{5}}-\phi) e^{\frac25 \pi}} = 1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}} {1+\frac{e^{-8\pi}} {1+\ldots} } } }
\end{equation*}
</pre>

<pre class="math">
\begin{equation*}
1 + \frac{q^2}{(1-q)}+\frac{q^6}{(1-q)(1-q^2)}+\cdots = \prod_{j=0}^{\infty}\frac{1}{(1-q^{5j+2})(1-q^{5j+3})}, \quad\quad \text{for $|q|<1$}.
\end{equation*}
</pre>

<pre class="math">
\begin{align} 
\nabla \times \vec{\mathbf{B}} -, \frac1c, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \newline \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \newline \nabla \times \vec{\mathbf{E}}, +, \frac1c, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \newline \nabla \cdot \vec{\mathbf{B}} & = 0
\end{align}
</pre>

<pre class="math">
\begin{equation} \label{eq:showcase}
x(t) = e^{\int_{t_0}^tp(s)ds}\Bigg(\int_{t_0}^t\Big(q(s)e^{-\int_{t_0}^sp(\tau)d\tau}\Big)ds + x_0\Bigg). 
\end{equation}
</pre>

We can even reference equation $$\eqref{eq:showcase}$$.



# Highlighting

Below is an example of some Python code highlighted using the builtin
`highlight` shortcode.
{{< highlight python >}}
    def f(x, h):
        return x + y
{{< /highlight >}}


# Images

Belowa are a few responsive images.

{{< figure src="/img/post/features/mt-fuji-and-sakura.jpg" title="Mt Fuji" >}}

{{< figure src="/img/post/features/napoleans-march.png" title="Napolean's march" >}}

# Lists

Below is an example of a list with long items.

- This is item one.  It is not so long.
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ut vulputate magna. Curabitur maximus leo sit amet arcu congue, et aliquet felis dictum. Donec a ullamcorper neque. Nulla suscipit sollicitudin rutrum.
- Another shorter item.

# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5

# Languages

初しぐれ猿も小蓑をほしげ也

# Quotes

Below is an example of blockquotes.

>  "For me, it is far better to grasp the Universe as it really is than to
>  persist in delusion, however satisfying and reassuring."
>
>  Carl Sagan

