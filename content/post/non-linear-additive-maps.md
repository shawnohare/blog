---
blogimport: true
date: 2013-03-29T17:27:00Z
markup: mmark
math: true
tags:
- linear algebra
title: Non-linear Additive Maps
updated: 2013-03-29T17:37:34Z
slug: c7b5f3e2-7b55-4a84-84b8-9ea6f91f84f0

---

While teaching an introductory linear algebra course, a colleague noticed that most of the examples of additive maps he gave turned out to be linear.  He asked whether I could think of a map which was additive, but not linear.  In a general context, the question was to find a ring $$R$$, $$R$$-modules $$ V$$ and $$ W$$, and a map $$ f \colon V \to W$$ such that $$ f $$ is a group homomorphism, but not an $$ R$$-module morphism, i.e, $$ f(x+y)=f(x)+f(y)$$ for all $$ x,y \in V,$$ but there is some $$ r \in R$$ and $$ z \in V$$ such that $$ f(r \cdot z) \neq r \cdot f(z)$$.



<!--more-->



One example that came to mind was viewing $$ \mathbb{C}$$ as a vector space over itself and taking $$ f \colon \mathbb C \to \mathbb C$$ to be the reflection $$ f(a+bi):=b+ai$$.  This map is readily seen to be a group endomorphism of $$ (\mathbb C, +)$$, but it does not commute with rotation counter-clockwise by by $$ \pi/2$$ radians, which is just multiplication by $$ i$$.  In particular, $$ f(i \cdot 1)=f(i)=1 \neq -1 = i^2 = i \cdot f(1)$$.
