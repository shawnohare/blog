---
blogimport: true
date: 2013-11-02T15:11:00Z
markup: mmark
math: true
tags:
- math
title: A Simple Proof that the Harmonic Series Diverges
updated: 2013-11-02T15:11:45Z
slug: 62d4e7ec-dd8a-4c4c-b31f-cdbaba92bafc

---

One usually encounters the harmonic series

$$\begin{equation*}
  \sum_{k=1}^{\infty} \frac{1}{k}
\end{equation*}$$

 as an example of a series that diverges for non-obvious reasons. With $$H_n$$ defined to be the partial sum $$H_n:=\sum_{k=1}^n \frac{1}{k}$$,  a typical way to prove divergence is to observe that

$$\begin{align*}
  H_{2n} &= H_n + \frac{1}{n+1} + \dots + \frac{1}{2n} \\  & \geq H_n + \underbrace{\frac{1}{2n} + \dots + \frac{1}{2n}}_{n \text{ terms}} \\  & = H_n + \frac{1}{2}.
\end{align*}$$

 In particular, $$H_{2^n} \geq 1 + \frac{n}{2}$$, so the sequence of partial sums of the harmonic series has an unbounded subsequence, whence the series diverges.

<!--more-->



The other day the author stumbled upon a simple proof of divergence.   Almost certainly this is not new, due to the simplicity of the argument. Suppose for the sake of a contradiction that the harmonic series converges to a number $$h$$.  Then

$$\begin{align*}
h &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6}\dots \\
  & \geq 1 + \frac{1}{2} + \left(  \frac{1}{4} + \frac{1}{4} \right) + \left( \frac{1}{6} + \frac{1}{6}  \right) + \dots \\  &= \frac{1}{2} + h,
\end{align*}$$

 an obvious contradiction.
