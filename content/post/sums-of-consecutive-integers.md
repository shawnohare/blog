+++
title = "Sums of Consecutive Integers"
date = 2013-03-29T16:47:00Z
updated = 2013-03-29T16:47:46Z
tags = ["math"]
markup = "mmark"
blogimport = true
math = true

+++

A fun fact I recently learned about is the following.

<b>Claim </b>.  A natural number can be written as the sum of at least two
consecutive positive integers if and only if it is not a power of 2.



<!--more-->

<i>Proof</i>.  Let $$ n = 2^s (2k+1)$$ for a positive integer $$ k$$ and
non-negative integer $$ s$$.  First suppose that $$ 2^s \gt 2k+1$$.   Then

$$\begin{align*}
\sum_{i=0}^{2k} (2^s - k +i)
&= 2^s (2k+1) - k (2k+1) + \sum_{i=1}^{2k} i \\
&= 2^s(2k+1) - k(2k+1) + k(2k+1)=2^s(2k+1) \\
&=n,
\end{align*}$$

so  $$ n$$ may be written as the sum of $$ 2k+1$$ consecutive positive
integers.   On the other hand, suppose that $$ 2^s \lt 2k+1$$.  Then it’s
straightforward to verify that $$ n = \sum_{i=0}^{2^{s+1} - 1} k-(2^s -1) +
i$$.  This demonstrates that if $$ n$$ is not a power of 2, then it can be
written as the sum of at least two consecutive positive integers.  Finally,
suppose that  can be written as the sum of at least two consecutive positive
integers.  Then there exists positive integers $$ k, m$$ such that

$$\begin{align*}
n 
&= \sum_{i=0}^m k + i = k(m+1) + m(m+1)(1/2) \\
&= (m+1)(2k+m)(1/2)
\end{align*}$$

If $$ m$$ is even, then 2 divides $$ 2k+m$$ and $$ m+1$$ is odd, whence $$ n$$
is divisible by some odd prime.  On the other hand, if $$ m$$ is odd, then 2s
divides $$ m+1$$ and $$ 2k+m$$ is odd, whence $$ n$$ is divisible by an odd
prime.  This demonstrates that  $$ n$$ is not a power of 2.
