+++
title = "The Continuum Hypothesis and Weird Probabilities"
date = 2013-12-05T22:40:00Z
updated = 2014-09-26T11:12:22Z
tags = ["math"]
markup = "mmark"
blogimport = true
math = true

+++

I recently heard of an interesting "proof" that $$(0,1)$$ does not have cardinality $$\aleph_1$$.  This would disprove the Continuum Hypothesis  ($$\textbf{CH}$$), which asserts that any subset of $$(0,1)$$ is either countable or has the same cardinality as $$(0,1)$$.   More precisely, $$\textbf{CH}$$ states that  if $$\omega_0$$ denotes the first countable ordinal (i.e., the set of natural numbers) and $$\omega_1$$ denotes the first uncountable ordinal, then   $$| \omega_1| = | 2^{\omega_0}|$$.  Here $$2^{\omega_0}$$ is the set of all binary-valued functions $$f \colon \omega_0 \to \{ 0, 1\}$$, which has the same cardinality as the power set of $$\omega_0$$ and as $$(0,1)$$.



<!--more-->



Before we launch into the so-called proof, we should mention a few things about the ordinal numbers.  By definition $$\omega_1$$ is the limit ordinal of all the countable ordinals, so in particular it is the set of all countable ordinals.  The well-ordering of $$\omega_1$$ is induced from set membership.  This means that given $$a, b \in \omega_1$$, we have $$a \lt b$$ if and only if $$a \in b$$.  As a consequence, the set $$M(b):=\{ a \in \omega_1 \mid a \lt b \}$$ is just $$b$$ itself, which we recall is countable.

<b>Proof.</b>  Assume for the sake of a contradiction that  $$I=(0,1)$$ has a well-ordering of length $$\omega_1$$. What this means is that we well-order $$I$$ in a way such that there is a poset isomorphism between $$I$$ and $$\omega_1$$.  In other words, we are assuming that $$\textbf{CH}$$ is true.   From now on when we write $$x \lt y$$ we mean with respect to this well-ordering, not the usual "less than or equal to" ordering of the reals.

You and I play a game. We both throw darts (randomly) at the interval $$(0,1)$$. Yours lands first at a number $$x$$ and then mine lands at a number $$y$$.  Since $$M(x)$$ is a countable set it has probability $$0$$, so $$x \lt y$$ with probability $$1$$.  That is, I almost always win!  Of course, the real number line has no way to know which dart hit first, so we could just as well argue that $$y \lt x$$ with probability $$1$$, showing that you should almost always win.  These two outcomes are incongruent, and so we cannot possibly have a well-ordering of $$(0,1)$$ with length $$\omega_1$$, whence $$\textbf{CH}$$ is disproved.  QED.

G\"{o}del and Cohen proved that $$\textbf{CH}$$ is independent from the usual ZFC axioms of set theory, which means that it cannot be proved or disproved using these axioms.  Our argument above does not rely on anything outside of ZFC, so it cannot possibly be a disproof of $$\textbf{CH}$$.

It's rather difficult to see what is amiss with the argument in its present form. In what follows we attempt to formalize the above proof a bit and explain why it breaks down.  The main idea is that reasoning with probabilities becomes a bit dodgy when constructing sets by invoking the Axiom of Choice, which we do when we well-order a set in light of the fact that the Axiom of Choice is equivalent to the Well-Ordering Principle. Basically, sets constructed in such manners are quite likely to be non-measurable.

<b>More formal proof.</b>For a fixed $$x \in (0,1)$$, the set $$M(x):=\{ y \in I \mid y \lt x \}$$ is countable, as argued above. It follows that almost all $$y \in (0,1)$$ satisfy $$x \lt y$$.   This then implies (here is the rub) that that almost all pairs $$(x,y) \in I^2$$ satisfy $$x\lt y$$,  so $$A:=\{ (x,y) \in I^2 \mid x \lt y \}$$ has measure $$1$$.  But due to symmetry, almost all pairs $$(x,y)$$ should  satisfy $$y \lt x$$, so $$B:=\{ (x,y) \in I^2 \mid y \lt x \}$$ should also have measure $$1$$.   But $$B$$ is contained in the compliment of $$A$$, so it must have measure $$0$$.  This is a contradiction.  QED.

The paradox has similarities to the Banach-Tarski paradox. Certain care is needed since the sets $$A$$ and $$B$$ are constructed with respect to the well-ordering of $$(0,1)$$ and so it's not immediately clear whether that they are in fact measurable.  The proof fails if $$A$$ and $$B$$ are not measurable.

We  claim that $$A$$ is non-measurable.  The horizontal sections of $$A$$ are countable while the vertical sections are  co-countable.  If $$A$$ were measurable, the Fubini-Tonelli theorem would imply that that the measure of $$A$$ was both $$1$$ and $$0$$.  Hence $$A$$ is not in fact measurable.

To see this last part in more detail, let  $$\chi_A \colon I^2 \to \mathbb R$$ denote the indicator function for $$A$$.  If $$y$$ is fixed then $$\chi_A(x,y)$$ is supported on a countable subset of $$I$$.  On the other hand, if $$x$$ is fixed then $$\chi_A(x,y)$$ is supported on a co-countable subset of $$I$$.   Were $$A$$ measurable we would have

$$\begin{align*}
  \mu(A)&=\iint_{I^2}  \chi_A (x,y) \ d(x,y) = \int_I \left( \int_I  \chi_A (x,y) \ dx\right) dy = \int_I 0 \ dy= 0 \quad \text{and} \\  \mu(A) &=\iint_{I^2}  \chi_A (x,y) \ d(x,y) = \int_I \left(  \int_I \chi_A (x,y) \ dy \right) dx =\int_I dx = 1,
\end{align*}$$

 where $$\mu$$ denotes the standard Lebesgue measure on $$\mathbb R^2$$.  This shows that $$A$$ is not in fact measurable, and so the "proof" above is flawed.
