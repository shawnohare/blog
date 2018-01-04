+++
title = "Symmetries of the Naturals"
date = 2013-03-29T17:23:00Z
updated = 2013-03-31T09:25:42Z
tags = ["math"]
markup = "mmark"
blogimport = true 
math = true

+++


This was a little problem I thought about while backpacking a few years ago.

We define a symmetry of the natural numbers to be any bijective function $$ f \colon \mathbb{N} \to \mathbb{N}$$.  Let $$ S$$ denote the set of symmetries of $$ \mathbb N$$.

<b>Claim</b>.  $$ S$$ has the cardinality of the continuum.



<!--more-->



<i>Proof</i>.  Since the symmetries of the naturals are contained in the set of all functions from the naturals to themselves, which itself is contained in the set of all relations on the naturals, we have $$ |S| \leq |\mathbb{N}^{\mathbb N}| \leq |\mathcal P(\mathbb N \times \mathbb N)| = |\mathcal P(\mathbb N)|=\mathfrak c$$.

To show the converse inequality it suffices to find a surjection from $$ S$$ to any set with the cardinality of the continuum, as this induces an injection in the opposite direction.  Consider the map $$ F \colon S \to \mathcal P(\mathbb N)$$, $$ f \mapsto \{ n \in \mathbb N \mid f(n)=n\}$$, which takes a symmetry to its set of fixed-points.  We claim  $$ F(S)=P:=\mathcal P(\mathbb N) \setminus \{ \mathbb N \setminus \{ m \} \mid m \in \mathbb N \}$$.  To see this, first observe that a symmetry of the naturals cannot have as fixed-points any set of the form $$ \mathbb N \setminus \{m\}$$, where $$ m \in \mathbb N$$, so $$ F(S) \subseteq P$$.    On the other hand, let $$ A \in P$$.  Then $$ \mathbb N \setminus A$$ is either empty or contains at least two elements.  We claim there exists a bijection $$ g_A \colon \mathbb N \setminus A \to \mathbb N \setminus A$$ that has no fixed-points.  If $$ A=\mathbb N$$ then this claim is vacuously true.  If $$ N \setminus A$$ is finite and contains $$ m \geq 2$$ elements, then any $$ m$$-cycle in the symmetric group on $$ m$$ letters is a bijection with no fixed points.  Finally, when $$ N \setminus A$$ is infinite we have $$ N \setminus A = \{ a_1, a_2, \dots, \}$$ for some natural numbers $$ a_i$$ with $$ i \in \mathbb N$$.  The function $$ g_A \colon \mathbb N \setminus A \to \mathbb N \setminus A$$ defined by $$ g_A(a_i)=a_{i+1}$$ if $$ i$$ is odd and $$ g_A(a_i)=a_{i-1}$$ if $$ i$$ is even is clearly a bijection with no fixed-points.  This establishes that for an arbitrary $$ A \in P$$, the coproduct $$ 1_A \coprod g_A$$ is a symmetry of the naturals whose set of fixed-points is precisely $$ A$$, proving $$ F(S) \subseteq P$$, whence equality.  But $$ P$$ is clearly uncountable as it is constructed by removing a countable number of elements from an uncountable set, so $$ \mathfrak c =|P| =|F(S)| \leq |S|$$, giving equality.  $$\square$$

<i>Alternative Proof.</i> To see that $$S$$ has a cardinality at least as large as the continuum we can exhibit a surjection from $$S$$ to the set $$B'$$ of all infinite binary strings that contain an infinite number of 0's and an infinite number of 1's.   To see why, first let $$B$$ denote the set of all infinite binary strings, $$B_0$$ the set of all infinite binary strings where 0 occurs finitely many times, and $$B_1$$ the set of all infinite binary strings where 1 occurs finitely many times.  First note that $$B_0 = \cup_{n \in \mathbb N} C_n$$, where $$C_n$$ is the set of binary strings with precisely $$n$$ occurrences of 0.  Each $$C_n$$ is countable as it is in bijective correspondence with $$\mathbb N^n$$, so $$B_0$$ is countable.  Similarly, $$B_1$$ is countable.   Now
$$B' = B \setminus (B_0 \cup B_1)$$, so $$|B'|=|B|=\mathfrak c$$ since removing a countable set from an uncountable set does not change its cardinality.  The desired surjection from $$S$$ to $$B'$$ is the map $$f \mapsto (f_n)$$, where $$f_n \equiv f(n) \mod 2$$. $$\square$$
