+++
title = "Ring Endomorphisms of the Reals"
date = 2014-04-24T14:05:00Z
updated = 2014-04-24T14:05:18Z
tags = ["math"]
markup = "mmark"
blogimport = true 
math = true

+++

Today we present a (mostly) algebraic proof that the only field endomorphism of the real numbers $$\mathbb R$$ is the identity map.  Many arguments of this fact invoke continuity, which we particularly try to avoid.  To be clear, we require in this discussion that ring morphisms fix the multiplicative identity.    First we recall that any characteristic $$0$$ field has a prime subfield isomorphic to the rationals $$\mathbb Q$$, so we will always assume characteristic $$0$$ fields contain $$\mathbb Q$$.


<!--more-->


It's not too difficult to see that any field endomorphism fixes the prime  subfield, regardless of characteristic.  For the characteristic $$0$$ case we can argue as follows.  Suppose  $$K$$ is a field with characteristic $$0$$ and  $$f \colon K \to K$$ is a ring homomorphism.   As $$f$$ is also an abelian group homomorphism, it is a $$\mathbb Z$$-module morphism, so  $$f(n \cdot x) = n \cdot f (x)$$ for any $$n \in \mathbb Z$$ and $$x \in K$$.   In particular, $$f$$ fixes $$\mathbb Z$$.  Let $$q \in \mathbb Q$$.   We may write $$q = n/m$$ where $$n$$, $$m \in \mathbb Z$$ with $$m \neq 0$$.  Then 

$$\begin{equation*}
  m f(q) = f(m) f(n/m) = f(m \cdot (n/m)) = f(n) = n, 
\end{equation*}$$

 which yields $$f(q) = n/m = q$$, showing that $$f$$ fixes $$\mathbb Q$$.

Next, let's restrict the case to when $$K = \mathbb R$$.  We claim that $$f$$ is a poset morphism, i.e, that $$x \leq y$$ implies $$f(x) \leq f(y)$$.  This relies on the fact that any positive real is the square of some other real.  Suppose then that $$x \leq y$$, so that $$y - x \geq 0$$.  There exists a $$z \in \mathbb R$$ such that $$z^2 = y - x$$.  Now $$f(y) - f(x) = f(y - x) = f(z^2) = f(z) f(z) \geq 0$$ implying $$f(y) \geq f(x)$$, as desired. 

Finally we claim that $$f \colon \mathbb R \to \mathbb R$$ is in fact the
identity map.  Let $$x \in \mathbb R$$ be arbitrary and suppose that $$f(x)
\neq x$$.  If $$x \lt f(x)$$, then we may pick a rational $$q$$ such that $$x
\lt q \lt f(x)$$.  Because $$f$$ is order preserving we have $$f(x) \leq 
f(q)=q$$, a contradiction.  On the other hand if $$f(x) \lt x$$ we may pick a
rational $$q$$ such that $$f(x) \lt q \lt x$$.  But then $$q = f(q) \leq
f(x)$$, a contradiction.  This proves that $$f$$ is the identity function, as
desired.

While we did have to invoke a topological property of the real numbers---namely that the rationals are dense in the reals---we avoided any continuity arguments and requirements that f was injective and by extension strictly monotone. 
