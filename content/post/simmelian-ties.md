+++
title = "Simmelian Ties"
date = 2014-11-21T13:27:00Z
updated = 2014-11-21T13:27:37Z
draft = true
markup = "mmark"
blogimport = true 
math = true

+++

Within a network or graph, a Simmelian tie is a 3-clique, ie., a 3-complete subgraph.  This concept extends obviously to any relation $$R$$ on a set $$X$$.  If we let 

$$\begin{equation*}
   S:=R \cap R^{\circ}:=\{ (x, y) \in R \mid (y, x) \in R \} 
\end{equation*}$$

 denote the symmetric sub-relation, then a Simmelian tie is a collection $$\{x, y, z\} \subseteq X$$ such that $$(x, y) \in S$$, $$(y, z) \in S$$ and $$(x, z) \in S$$.  

<!--more-->


 Further associated to $$R$$ is a $$\mathbb Z$$-linear map $$T_R$$ sending $$x \mapsto \sum_{
