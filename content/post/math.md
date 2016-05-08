+++
date = "2015-12-09T17:23:10-07:00"
updated = "2016-05-07T09:55:48-07:00"
title = "Post with Mathematics"
description="Showcase some of the blog's features."
tags = ["sample", "latex", "mathjax"]
showPostTimes = true
+++

This post primarily serves as an example post to very specifically test
how mathematics markup like $\LaTeX$ is rendered.  The treatment of
LaTeX in markdown does not seem to be uniform across processors.  Our
hope is that these notes help to tease out edge cases.

<!--more-->

# Inline
Inline math sometimes is wrapped in code tags, but this paragraph contains the
two beautiful espressions $e^{i \pi} + 1 = 0$ and \\(\frac{d}{dx}(e^x) = e^x\\)
written in "naked" $\LaTeX$.

The paragraph above in markdown form looked like:
```latex
Inline math sometimes is wrapped in code tags, but this paragraph contains the
two beautiful espressions $e^{i \pi} + 1 = 0$ and \\(\frac{d}{dx}(e^x) = e^x\\)
written in "naked" $\LaTeX$.
```

# Display

Some guides suggest that display math be wrapped in paragraph or div tags.
This depends heavily on the markdown processor and MathJax configuration.
Below, we present two ways of rendering display mathematics.

The tensor product construction for bisets induces a bilinear map 
$$
  -- \cdot_H -- \colon B(G,H) \times B(H, K) \to B(G, K),
  \quad ([X], [Y]) \mapsto [X \times_H Y],
$$
between Burnside rings.

The tensor product construction for bisets induces a bilinear map 
\\[
  -- \cdot_H -- \colon B(G,H) \times B(H, K) \to B(G, K),
  \quad ([X], [Y]) \mapsto [X \times_H Y],
\\]
between Burnside rings.

These two paragraphs appeared in the markdown source as:
```latex
The tensor product construction for bisets induces a bilinear map 
$$
  -- \cdot_H -- \colon B(G,H) \times B(H, K) \to B(G, K),
  \quad ([X], [Y]) \mapsto [X \times_H Y],
$$
between Burnside rings.

The tensor product construction for bisets induces a bilinear map 
\\[
  -- \cdot_H -- \colon B(G,H) \times B(H, K) \to B(G, K),
  \quad ([X], [Y]) \mapsto [X \times_H Y],
\\]
between Burnside rings.
```

# Escaping

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


# Environments 

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

```
Suppose we wish to use an `align` environment.  Some markdown processors
will convert the newline LaTeX `\\` to `\`.  One work around is to escape
both slashes.  For example:
\begin{align}
  x^2 &= 1 \\\\
  x^2 -1 &= 0 \\\\
  (x-1)(x+1) &= 0
\end{align}
```

# Labels

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
