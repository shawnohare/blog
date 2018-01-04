+++
title = "Law of Iterated Expectation"
date = 2014-07-07T20:56:00Z
updated = 2014-07-08T08:15:56Z
tags = ["probability"]
markup = "mmark"
blogimport = true
math = true

+++

Let $$X$$ and $$Y$$ denote continuous, random, real-valued variables with joint
probability density function $$f(X, Y)$$.  The marginal density function of
$$Y$$ is $$f_Y(y) := \int_{x \in \mathbb R} f(x, y) dx$$. The expectation
$$E(Y)$$ of $$Y$$ can be recovered by integrating against the marginal density
function.  In particular,

$$\begin{equation} \label{eq:E(Y)}
E(Y)=\int_{y \in \mathbb R} y f_Y(y) dy
= \int_{y \in \mathbb R} \int_{x \in \mathbb R} y f(x, y) \ dx \ dy.
\end{equation}$$

The conditional probability density function of $$Y$$ given that $$X$$ is equal
to some value $$x$$ is defined by

$$\begin{equation} \label{eq:cdf} 
f_{Y \mid X} (y \mid X = x)
:= f_{Y \mid X} (y \mid x)
= \frac{f(x, y)}{f_X(x)}
= \frac{f(x,y)}{\int_{y \in \mathbb R} f(x, y) \ dy}.
\end{equation}$$

The conditional expectation $$E(Y \mid X = x)$$ of $$Y$$ given that $$X$$ has
value $$x$$ is given by

$$\begin{equation} \label{eq:cond exp}
E(Y \mid X = x)
= \int_{y \in \mathbb R} y f_{Y \mid X} (y \mid x) \ dy.
\end{equation}$$

But $$E(Y \mid X = x)$$ depends on $$X$$, so in turn is itself a random
variable denoted $$E(Y \mid X)$$, whence we can compute its expectation.  Now

$$\begin{align*}
E (E (Y \mid X))
&= \int_{x \in \mathbb R} E(Y \mid x) f_X(x) \ dx \\
&= \int_{x \in \mathbb R} f_X(x) \left( \int_{y \in \mathbb R} y f_{Y \mid X}(x, y) \ dy  \right) \ dx \quad \text{(by \ref{eq:cond exp} )} \\ 
& = \int_{x \in \mathbb R} \int_{y \in \mathbb R} f_X(x) 
\cdot  y \frac{f(x,y)}{f_X(x)} \ dy \ dx  \quad \text{(by \ref{eq:cdf})}\\
& = \int_{y \in \mathbb R} \int_{x \in \mathbb R} y f(x, y) \ dx \ dy \\
& = E(Y). \quad \text{(by \ref{eq:E(Y)})}
\end{align*}$$

 This result is sometimes called the <b>law of the iterated expectation</b>.
