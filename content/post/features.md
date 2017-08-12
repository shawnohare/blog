+++
date = "2015-12-09"
updated = "2017-05-29"
title = "Features"
description="Showcase some of the blog's features."
tags = ["multi word tag", "sample", "latex", "mathjax"]
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

For example, {{< inline "`$\sum_{n \in \mathbb{N}} \frac{1}{n^2}$`" >}} 
is rendered from
```
{{</* inline "\`$\sum_{n \in \mathbb{N}} \frac{1}{n^2}$\`" */>}}
```

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


### Long Display

Below is an example of displayed math that contains a single, long line.

{{< display >}}
```
\begin{equation*}
   \iiint_{\mathbb R^3} 1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^{10} + x^{11} + x^{12}
   - (1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^{10}) \ dx
\end{equation*}
```
{{< /display >}}


## Environments 

Basic environments and references are a feature of MathJax.

For example, the degree 2 cyclotomic polynomial
{{< display >}}
\begin{equation}\label{eq:example}
  x^2 + 1 = 0 
\end{equation}
{{< /display >}}
We can now reference $\eqref{eq:example}$ via `$\eqref{eq:example}$`.

Even `align` environments work as expected:
{{< display >}}
```
\begin{align*}
  x^2 &= 1 \\
  x^2 -1 &= 0 \\
  (x-1)(x+1) &= 0.
\end{align*}
```
{{< /display >}}

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

