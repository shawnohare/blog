+++
title = "Densities and Expectations"
date = 2013-06-24T11:40:00Z
updated = 2014-07-07T20:01:13Z
markup = "mmark"
blogimport = true 
math = true

+++

For the layperson, it's probably most helpful to think of the density function $$f$$ associated to a random variable $$X$$ as the function you integrate to compute probabilities.  Similarly, the expected value $$E(X)$$ is thought of as the average value that $$X$$ takes.  Often $$E(X)$$ is defined already in terms of the density function, and it's not clear to the beginner why $$\int_{\mathbb R} x f(x) \ dx$$ should compute the expected value of $$X$$.  What should be perhaps a bit more obvious is that if you integrate $$X$$ over the entire probability space, with respect to the given probability measure, then you obtain the average value of $$X$$.  This is indeed how the expectation of $$X$$ is typically defined in a more analytical setting.


<!--more-->


Given an arbitrary measure space $$(\Omega, \mathcal B, P)$$, a measurable space $$(\Omega, \mathcal B')$$, and a $$(\mathcal B, \mathcal B')$$-measurable map $$X \colon \Omega \to \Omega'$$, the pushforward $$P_X(E):=P(X^{-1} (E))$$ is a measure on $$\Omega'$$.  It is easy to verify that if $$f \colon \Omega' \to \mathbb R$$ is any measurable function, then $$\int_{\Omega'} f \ dP_X = \int_{\Omega} (f \circ X) \ dP$$. 

Now we us restrict ourselves to the context of a probability space $$(\Omega, \mathcal B, P)$$.  A random variable $$X \colon \Omega \to \mathbb R$$ is $$(\mathcal B, \mathcal B')$$-measurable, where $$\mathcal B'$$ denotes the Borel subsets of $$\mathbb R$$. The expectation $$E(X)$$ of $$X$$ is defined to be $$\int_{\Omega} X \ dP$$.  In light of the proposition above, with $$1_{\mathbb R} \circ X$$ replacing $$f \circ X$$ (where $$1_{\mathbb R}$$ is the identity function on $$\mathbb R$$), we have 

$$\begin{equation*}
  E(X) =  \int_{\Omega} X \ dP=  \int_{\Omega} 1_{\mathbb R} \circ X \ dP =\int_{\mathbb R} 1_{\mathbb R} \ d P_X= \int_{\mathbb R} x \ d P_X. 
\end{equation*}$$

 The pushforward measure $$P_X$$ gives rise to, and is determined by, a function called the distribution function of $$X$$, defined by $$F(t):=P_X( (-\infty, t]) = P(X \leq t)$$.   The density function $$f$$ of $$X$$ is taken to be the Radon-Nikodym derivative $$d P_X/ d \lambda$$, where $$\lambda$$ is the usual Lebesgue measure on $$\mathbb R$$.  This means that for any Borel set $$B$$, the density  $$f$$ satisfies 

$$\begin{equation*}
  P(X \in B) = \int_{X^{-1}(B)} \ dP = \int_B f \ d \lambda = \int_B f \ dx.  
\end{equation*}$$

 One of the properties of the Radon-Nikodym derivative is that if $$g \colon \mathbb R \to \mathbb R$$ is $$P_X$$-measurable, then $$\int_{\mathbb R} g \ d P_X = \int_{\mathbb R} g \cdot (d P_X/d \lambda) \ d \lambda = \int_{\mathbb R} g \cdot f \ d \lambda$$. The identity function on $$\mathbb R$$ is $$P_X$$-measurable, so    

$$\begin{equation*}
  E(X) = \int_{\mathbb R} x \ d P_x = \int_{\mathbb R} x \cdot f(x) \ dx,  
\end{equation*}$$

 which recovers the usual definition of the expectation in terms of the density.
