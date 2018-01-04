+++
title = "Simple Divisibility Tests"
date = 2013-11-12T12:14:00Z
updated = 2013-11-12T12:14:36Z
tags = ["math"]
markup = "mmark"
blogimport = true 
math = true

+++

In this post we will justify some common divisibility tests that most school children are familiar with.  Recall that a number such as $$111$$ is divisible by $$3$$ if and only if the sum of the digits is  divisible by $$3$$.  Since $$1+1+1=3$$ is divisible by $$3$$,  we see that $$111$$ is divisible by three.  

More generally, an integer $$N$$ is divisible by $$3$$ if and only if the sum of the digits appearing in $$N$$ is divisible by $$3$$. <div>


<!--more-->


This can be proven quite easily using modular arithmetic.   Recall that an integer $$N$$ with decimal expansion $$N=a_n a_{n-1} \dots a_1 a_0$$ can be written as 

$$\begin{equation*}
  N = \sum_{k=0}^n a_k 10^k. 
\end{equation*}$$

 Here $$a_k \in \{ 0, 1, \dots, 9 \}$$ for each $$k=1, \dots, n$$.   Since $$10^k \equiv 1 \mod 3$$ for any natural number $$k$$, we see that 

$$\begin{equation*}
  N \equiv \sum_{k=0}^n a_k \mod 3. 
\end{equation*}$$

 This proves the claim.</div><div>
Since $$10^k \equiv 1 \mod 9$$ for each natural number $$k$$, the same divisibility test holds for $$9$$ as well.  That is, a number $$N$$ is divisible by $$9$$ if and only if the sum of its digits is divisible by $$9$$.  

A similar observation gives a divisibility test for $$11$$. Note that $$10^k \equiv (-1)^k \mod 11$$ for any natural number $$k$$, so $$N = a_n \dots a_0$$ satisfies 

$$\begin{equation*}
  N \equiv \sum_{k=0}^n (-1)^k a_k \mod 11. 
\end{equation*}$$

 This $$N$$ is divisible by $$11$$ if and only if the alternating sum of its digits is divisible by $$11$$.  </div>
