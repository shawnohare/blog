+++
date = "2016-06-05T11:36:21-07:00"
description = "An exercise about expectation."
math =  true
categories = ["probability"]
tags = ["exercise", "expectation"]
title = "Expected number of coin tosses for consecutive heads or tails"

+++

A fun elementary exercise involving expectation is to compute the number of
times we expect to toss a coin before seeing consecutive heads or tails.

<!--more-->

Let $p_n$ denote the probability that it takes us $n \geq 2$ tosses to
witness the first occurrence of consecutive heads or tails.  Of all the
$2^n$ possible sequences of flips, there are only $2$ that satisfy
the condition that the last two flips are identical and the first $n-1$
flips are strictly alternating.  For example, if it took us 3 tosses
then we either observed the sequences HTT or THH.  Thus we have

{{< display >}}
```
\[
  p_n = \frac{2}{2^{n}} = 2^{1-n}.
\]
```
{{< /display >}}

These probabilities $p_n$ define a discrete probability distribution over
the natural numbers.  The expectation (or mean value) of this
distribution is precisely the number of coin tosses needed to observe
consecutive heads or tails. Letting $E$ denote this expectation, we have
by definition

{{< display >}}
```
\begin{align}
  E &= \sum_{n=2}^{\infty} n \cdot p_n \\
  &= \sum_{n=2}^{\infty} \frac{n}{2^{n-1}} \label{eq:def}.
\end{align}
```
{{< /display >}}

The right-hand expression \eqref{eq:def} can now be split into a series 
whose terms are themselves geometric series via

{{< display >}}
```
\begin{align*}
  \eqref{eq:def} &= \left(\sum_{n=2}^{\infty} \frac{1}{2^{n-1}} \right)
    + \sum_{n=2}^{\infty} \left( \sum_{j=n}^{\infty} \frac{1}{2^{j-1}} \right) \\
  &= \sum_{n=1}^{\infty} \frac{1}{2^{n}}
    + \sum_{n=1}^{\infty} \sum_{j=n}^{\infty} \frac{1}{2^{j}} \\
  & = 1 + \sum_{n=1}^{\infty} \frac{1}{2^{j-1}} \\
  &= 3. \\
\end{align*}
```
{{< /display >}}

We have thus proven that the expected number of coin tosses is in fact only 3.






