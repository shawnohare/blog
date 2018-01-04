+++
title = "A natural isomorphism between a vector space and its double dual."
date = 2013-07-27T17:27:00Z
updated = 2013-07-27T17:31:31Z
markup = "mmark"
blogimport = true 
math = true

+++

Soon after one begins a study of abstract vector spaces, they are confronted with the fact that a finite dimensional vector space is naturally (or canonically) isomorphic to its double dual space.  Intuitively, this means that the isomorphism is somehow independent of any particular choice of basis.  This notion is made rigorous  with the notion of natural transformations of functors between categories.



<!--more-->



For a finite dimensional vector space $$V$$ over a field $$K$$, there is a natural isomorphism $$V \to V^{**}$$ sending a vector $$v$$ to the evaluation at $$v$$ map $$\eta_{v} \colon V^* \to  K$$, $$v^* \mapsto v^*(v)$$.

More formally, let $$\mathcal C$$ denote the category of finite dimensional vector spaces over a fixed field.  Then the assignment of the isomorphisms $$\eta_V  \colon V \to V^{**}$$, $$v \mapsto \eta_v$$ for each $$V$$ gives a natural transformation $$\eta$$ between the identity functor  on $$\mathcal C$$ and the double dual functor  $$ (  - ) ^{**} \colon \mathcal C \to \mathcal C$$, which can be defined as the self-composition of the (contravariant) dual functor  $$(-)^* \colon \mathcal C \to \mathcal C$$ sending a linear map $$\varphi \colon V \to W$$ to the pre-composition with $$\varphi$$ map $$\varphi^* \colon W^* \to V^*$$,  $$w^* \mapsto w^* \circ \varphi$$.  Then $$\varphi^{**} \colon V^{**} \to W^{**}$$ is given by $$\varphi^{**}(v^{**}) = v^{**} \circ \varphi^*$$, which is itself a map defined by $$v^{**} \circ \varphi^* (w^*) = v^{**} (w^* \circ \varphi)$$.   In other words, 

$$\begin{equation*}
  \varphi^{**} \colon V^{**} \to W^{**}, \quad v^{**} \mapsto (w^* \mapsto v^{**} ( w^* \circ \varphi)). 
\end{equation*}$$



Let's now check that $$\eta$$ is actually a natural transformation.  To this end, suppose $$\varphi \colon V \to W$$ is a linear map.  We must verify that $$\varphi^{**} \circ \eta_V = \eta_W \circ \varphi$$.  Given $$v \in V$$, we have $$[\varphi^{**} \circ \eta_V] (v) = \varphi^{**} (\eta_v) = \eta_v \circ \varphi^*$$.   For $$w^* \in W^*$$, it follows that $$[\eta_v \circ \varphi^*] (w^*) = \eta_v (w^* \circ \varphi) = w^* ( \varphi(v))$$.  On the other hand, $$[\eta_W \circ \varphi](v)=\eta_{\varphi(v)}$$ and $$\eta_{\varphi(v)}(w^*) = w^* (\varphi(v)$$, so the claim is established.
