+++
date = "2015-12-09T17:23:10-07:00"
updated = "2016-05-07T09:55:48-07:00"
title = "Features"
description="Showcase some of the blog's features."
tags = ["multi word tag", "sample", "latex", "mathjax"]
showPostTimes = true
+++

This post primarily serves as an example post to very specifically test
the various features provided by blog themes.  In particular,
how mathematics markup like $\LaTeX$ is rendered.  The treatment of
LaTeX in markdown does not seem to be uniform across processors.  Our
hope is that these notes help to tease out edge cases.

<!--more-->

# Math

## Inline
Inline math sometimes is wrapped in code tags, but this paragraph contains the
two beautiful espressions $e^{i \pi} + 1 = 0$ and \\(\frac{d}{dx}(e^x) = e^x\\)
written in "naked" $\LaTeX$.

The paragraph above in markdown form looked like:
```latex
Inline math sometimes is wrapped in code tags, but this paragraph contains the
two beautiful espressions $e^{i \pi} + 1 = 0$ and \\(\frac{d}{dx}(e^x) = e^x\\)
written in "naked" $\LaTeX$.
```

## Display

Some guides suggest that display math be wrapped in paragraph or div tags.
This depends heavily on the markdown processor and MathJax configuration.
Below, we present two ways of rendering display mathematics.

The tensor product construction for bisets induces a bilinear map

$$
  -- \cdot_H -- \colon B(G,H) \times B(H, K) \to B(G, K),
  \quad ([X], [Y]) \mapsto [X \times_H Y],
$$

between Burnside rings.

Source:

```latex
The tensor product construction for bisets induces a bilinear map

$$
  -- \cdot_H -- \colon B(G,H) \times B(H, K) \to B(G, K),
  \quad ([X], [Y]) \mapsto [X \times_H Y],
$$
```

The tensor product construction for bisets induces a bilinear map

\\[
  -- \cdot_H -- \colon B(G,H) \times B(H, K) \to B(G, K),
  \quad ([X], [Y]) \mapsto [X \times_H Y],
\\]

between Burnside rings.

Source:

```
The tensor product construction for bisets induces a bilinear map

\\[
  -- \cdot_H -- \colon B(G,H) \times B(H, K) \to B(G, K),
  \quad ([X], [Y]) \mapsto [X \times_H Y],
\\]

between Burnside rings.
```

### Long Display

Consider

\\[
   \iiint_{\mathbb R^3} 1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^{10}
   - (1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^{10} \ dx
\\]

## Escaping

In the display math example above we escaped the standard LaTeX display math
delimiters `\[ ... \]` with an extra `\`. Similar symbols must be escaped.
Of particular note are curly braces.  For instance,  the even numbers
$\\{ z \in \mathbb{Z} \mid z = 0 \mod 2 \\}$ can be written as
`\\{ z \in \mathbb{Z} \mid z = 0 \mod 2 \\}`.

The whole paragraph above is rendered from:
```latex
In the display math example above we escaped the standard LaTeX display math
delimiters `\[ ... \]` with an extra `\`. Similar symbols must be escaped.
Of particular note are curly braces.  For instance,  the even numbers
$\\{ z \in \mathbb{Z} \mid z = 0 \mod 2 \\}$ can be written as
`\\{ z \in \mathbb{Z} \mid z = 0 \mod 2 \\}`.
```


## Environments (Basic)

Most environments render normally.
For example, the degree 2 cyclotomic polynomial
\begin{equation}\label{eq:example}
  x^2 + 1 = 0 \iff x = \pm i
\end{equation}
renders just fine.

```
Most environments render normally.
For example, the degree 2 cyclotomic polynomial
\begin{equation}\label{eq:example}
  x^2 + 1 = 0 \iff x = \pm i
\end{equation}
renders just fine.
```

Suppose we wish to use an `align` environment.  The Hugo markdown processor
will convert the newline Latex `\\` to `\`.  One work around is to escape
both slashes.  For example:
\begin{align}
  x^2 &= 1 \\\\
  x^2 -1 &= 0 \\\\
  (x-1)(x+1) &= 0
\end{align}

The source is:
```
\begin{align}
  x^2 &= 1 \\\\
  x^2 -1 &= 0 \\\\
  (x-1)(x+1) &= 0
\end{align}
```

However, the  `\\\\` escape technique above seems to not work
with all Markdown processors. A more robust solution is to use
the technique is to use `\cr`.  Replacing `\\\\` with `\cr` in the source
above yields:

\begin{align}
  x^2 &= 1 \cr
  x^2 -1 &= 0 \cr
  (x-1)(x+1) &= 0
\end{align}

The source is:
```
\begin{align}
  x^2 &= 1 \cr
  x^2 -1 &= 0 \cr
  (x-1)(x+1) &= 0
\end{align}
```

## Environment (Complicated)

Environments beyond the basic types do not always render propertly.
For instance, using a label to mark a specific line an equation seems to confuse
certain markdown processors. Wrapping the environment in
`<div>` or `<section>` tags helps.

<div>
\begin{align}
  E &= \sum_{n=2}^{\infty} n \cdot p_n \cr
  &= \sum_{n=2}^{\infty} \frac{n}{2^{n-1}} \label{eq:def}.
\end{align}
</div>

The source is:
```
<div>
\begin{align}
  E &= \sum_{n=2}^{\infty} n \cdot p_n \cr
  &= \sum_{n=2}^{\infty} \frac{n}{2^{n-1}} \label{eq:def}.
\end{align}
</div>
```

# Code

We have seen examples of inline and block code styling in the previous
examples. Inline styling tends to be minimally intrusive, and utilizes
`monospace` font and a border to help distinguish it from prose. The
border is particularly useful longer code snippets, such as
`cat features.mid | grep Code`.


# Images

Belowa are a few responsive images.

{{< figure src="/img/post/features/mt-fuji-and-sakura.jpg" title="Mt Fuji" >}}

{{< figure src="/img/post/features/napoleans-march.png" title="Napolean's march" >}}

## Labels

We can reference equation \ref{eq:example} using the usual LaTeX syntax
of `\ref{eq:example}`.

```
We can reference equation \ref{eq:example} using the usual LaTeX syntax
of `\ref{eq:example}`.
```

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

>  For me, it is far better to grasp the Universe as it really is than to
>  persist in delusion, however satisfying and reassuring.
>
>  Carl Sagan

