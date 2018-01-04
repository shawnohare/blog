+++
title = "Distributions, Densities, and Mass Functions"
date = 2014-07-01T16:52:00Z
updated = 2014-09-26T11:26:10Z
tags = ["probability"]
markup = "mmark"
blogimport = true 
math = true

+++

One unfortunate aspect of probability theory is that common measure theoretic
constructions are given different, often conflated, names.  The technical
definitions of the probability distribution, probability density function, and
probability mass function for a random variable are all related to each other,
as this post hopes to make clear. 

We begin with some general measure theoretic constructions. Let $$(A, \mathcal
A)$$ and $$(B, \mathcal B)$$ be measurable spaces and suppose that $$\mu$$ is a
measure on $$(A, \mathcal A)$$.   Any $$(\mathcal A, \mathcal B)$$-measurable
function $$X \colon A \to B$$ induces a push-forward measure
$$X_*(\mu)$$ on $$(B, \mathcal B)$$ via: 

$$\begin{equation*}
[X_*(\mu)](S \in \mathcal B):= \mu(X^{-1} (S)). 
\end{equation*}$$
 

<!--more-->


Any function $$f \colon A \to [0, \infty)$$ induces a measure $$\mu$$ on $$(A,
2^A)$$ via integration against the counting measure $$\nu$$. This can be seen
as a converse to the Lebesgue-Radon-Nikodym theorem. More specifically, 

$$\begin{equation*}
\mu(S \subseteq A)
:=\int_S f d \nu
:= \sup_{R \subseteq S, |S| \lt \infty} \sum_{r \in R} f(r)
=: \sum_{s \in S} f(s). 
\end{equation*}$$

  

A probability space is simply a measure space $$(A, \mathcal A, P)$$ such that
$$P(A)=1$$.   Often $$A$$ is called the sample space, $$\mathcal A$$ the
event space and $$P$$ the probability measure. An $$(\mathcal A,
\mathcal B)$$-measurable function $$X$$ is called a random variable and
the push-forward probability measure $$X_*(P)$$ on $$(B, \mathcal B)$$ is
called the distribution of $$X$$.  The probability density function
$$f$$ of $$X$$ with respect to a measure $$\mu$$ on $$(B, \mathcal B)$$ is
a Radon-Nikodym derivative $$d X_*(P)/ d \mu$$, provided it exists.  Therefor
$$f$$ satisfies 

$$\begin{equation*}
P(X \in S) := P(X^{-1}(S)) = \int_{X^{-1}(A)} dP = \int_A f d \mu 
\end{equation*}$$

 for all $$\mathcal B$$-measurable sets $$S$$.

The waters are slightly muddied by the fact that these general constructions
often go by different names in the discrete case. We say a measurable space
$$(A, \mathcal A)$$ is discrete provided that $$A$$ is a countable set, and a
random variable $$X \colon A \to B$$ is a discrete random variable provided
that the image of $$X$$ is countable and the pre-images of singleton sets are
measurable.  When the $$\sigma$$-algebra $$\mathcal B$$ on $$B$$ is
discrete---which simply means that $$\mathcal B$$ is the power set of $$B$$---
then $$X$$ is discrete provided its image is countable, since $$X$$ is
measurable. 

A probability mass function $$f_X \colon B \to [0, \infty]$$  of a discrete
random variable $$X \colon A \to B$$ is typically defined to be a  function
such that $$P(X=b):=P(X^{-1}(b))=f_X(b)$$ for all $$b \in B$$.   It's possible
to view a probability mass function as both a restriction of a distribution of
$$X$$ and as a probability density function of $$X$$ with respect to the
counting measure.  To see the former, recall that the distribution of $$X$$ is
just the push-forward measure $$X_*(P)$$ on $$(B, \mathcal B)$$.  If $$\mathcal
B$$ is in fact the discrete $$\sigma$$-algebra, then for all $$b \in B$$ we
have 

$$\begin{equation*}
P(X = b):=P(X^{-1}(b))=[X_*(P)] (\{b\}). 
\end{equation*}$$

Defining $$f \colon B \to \mathbb R$$ to be the restriction of the distribution
$$X_*(P)$$ to singleton sets, in the sense that  $$f(b):=[X_*(P)] (\{b\})$$,
clearly yields a probability mass function for $$X$$. 

Now further assume that the the density function $$f$$ of $$X$$ with respect to the counting measure $$\nu$$ on $$(B, \mathcal B)$$ exists.   Then for all $$b \in B$$ we have 

$$\begin{equation*}
f(b)
= \sum_{x \in \{b\}} f(x)
= \int_{\{b\}} f d \nu 
= \int_{X^{-1}(b)} dP
= P(X^{-1}(b)). 
\end{equation*}$$

 This density function then is nothing other than a probability mass function. 

Let's put some of this into a specific context.  Suppose we toss $$n$$ coins
that are all weighted to come up heads with probability $$\theta$$. If all
these coins are tossed, what's the probability we see $$k \leq n$$ heads? It's
fairly easy to see that this is given by the binomial distribution $$f_{\theta,
n}(k):= \binom{n}{k}\theta^k (1-\theta)^{n-k}$$.  Is $$f_{\theta, n}$$ actually
a distribution of some random variable? 

As a sample space for this experiment we can take the set of all $$n$$ coin
tosses, which mathematically is just the set of length $$n$$ binary strings.
So define $$A:=\{0, 1 \}^n$$ and let $$(A, 2^A)$$, $$(\mathbb N, 2^{\mathbb
N})$$ denote discrete measurable spaces with discrete $$\sigma$$-algebras.
Further, let $$(\mathbb R, \mathcal B)$$ denote $$\mathbb R$$ equipped with the
usual Borel $$\sigma$$-algebra. Any function from $$A$$ to the naturals is
$$(2^A, 2^{\mathbb N})$$-measurable, and similarly any function $$\mathbb N \to
\mathbb R$$ is $$(2^{\mathbb N}, \mathcal B)$$-measurable.  In particular the
summation function $$Y \colon A \to \mathbb N$$ defined 

$$\begin{equation*}
Y((a_1, a_2, \dots, a_n)) := \sum_{i=1}^n a_i 
\end{equation*}$$

is measurable as is the function $$Y' \colon \mathbb N \to \mathbb R$$ defined
by $$Y'(k)=\theta^k (1-\theta)^{n-k}$$.  The composition $$X := Y' \circ Y$$ is
a measurable function and since it's  always non-negative it induces a measure
$$P$$  on $$(A, 2^A)$$ defined by 

$$\begin{equation*}
P(S \subseteq A):=\sum_{s \in S} X(s) = \sum_{s \in S}.  
\end{equation*}$$

This measure generalizes the counting measure.  Now 

$$\begin{align*}
P(A) &= \sum_{a \in A} X(a) \\     &= \sum_{a \in A} \theta^{Y(a)}(1-\theta)^{Y(a)} \\     & = (\theta + (1- \theta))^n \\     & = 1, 
\end{align*}$$

so in fact the measure $$P$$ is a probability measure.  The push-forward
measure $$Y_*(P)$$ on $$(\mathbb N, 2^{\mathbb N})$$ satisfies, for each $$k
\in \mathbb N$$, 

$$\begin{align*}
[Y_*(P)](\{k\}) & = P(Y^{-1}(k)) \\     & = \sum_{a \in Y^{-1}(k)} X(a) \\     & = \sum_{a \in Y^{-1}(k)} \theta^k (1-\theta)^{n-k} \\     & = \binom{n}{k} \theta^k (1-\theta)^{n-k} \\     & = f_{\theta, n}(k). 
\end{align*}$$

 This indeed shows that the binomial distribution  $$f_{\theta, n}$$ is the
 restriction of the distribution  (with respect to $$P$$) of the number of
 heads random variable $$Y$$. 

Initially we started only with a sample space, some random variable $$Y$$ of
interest, and a method of assigning probabilities to individual elements in the
sample space via this random variable, and a parameter $$\theta$$.  We did not
need to initially specify a probability measure on the sample space, since this
was later induced by $$\theta$$ and $$Y$$. 

Very often the underlying sample space is ignored completely, and only a
density function $$f \colon B \subseteq \mathbb R \to [0, \infty)$$ for a
random variable is specified.   This is because we can recover the distribution
(push-forward) of a random variable from its density function alone. For
simplicity suppose that $$(A, \mathcal A)$$ and $$(B \subseteq \mathbb R,
\mathcal B)$$ are measurable spaces and that $$X \colon A \to B$$ is a random
variable.  If $$X$$ is discrete, take $$\mathcal B:=2^B$$, $$\mathcal A:=2^A$$,
and let $$\nu$$ denote the counting measure.  Otherwise, let $$(B, \mathcal
B)$$ denote the reals together with the Borel $$\sigma$$-algebra and let
$$\nu$$ denote the Lebesgue measure.  We obtain a measure $$\mu$$ on $$(B,
\mathcal B)$$ by integrating $$f$$ against $$\nu$$: 

$$\begin{equation*}
\mu(S \in \mathcal B):=\int_S f d \nu. 
\end{equation*}$$

Now $$\nu$$ is always a $$\sigma$$-finite measure and if $$f$$ is suitably nice
(as probability densities are required to be) then $$\mu$$ is also
$$\sigma$$-finite and $$\mu$$ is absolutely continuous with respect to $$\nu$$,
so $$f$$ is in fact a Radon-Nikodym derivative of $$\mu$$. 
