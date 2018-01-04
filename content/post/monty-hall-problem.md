+++
title = "The Monty Hall Problem"
subtitle = "An exploration of probabilistic intuition"
date = 2013-09-19T04:53:00Z
tags = ["probability"]
markup = "mmark"
blogimport = true
math = true
draft = true

+++

# Introduction

The Monty Hall Problem is a puzzle originating in a gameshow.
A contestant stands before three doors, only one of which contains a prize.
Goats (i.e., non-prizes) stand behind the remaining doors.
The contestant chooses a door that they believe hides the prize. Monty, the host,
then reveals a goat from behind one of the other two doors not chosen.
At this stage, two doors remain closed and the contestant is given a choice
to open either door. Which door should the contest open?


<!--more-->

#  Incorrect Intuition

Many people assume that it does not matter which door the contestant opens,
because now the prize lies behind each door with equal probability.  While this
certainly appeals to our intuition in some basic sense, it's also equivalent
to the assertion that Monty's revelation somehow induces a re-sampling, which
should strike one as a tad odd.


# Bayesian Updates

We can use Bayes' rule as a natural way to account for the information update
that occurs after Monty's reveal.  Let $$A$$ be the door the contestant
originally chose, $$B$$ the remaining unopened door, and $$C$$ the door that
Monty opened to reveal a goat. We wish to calculate the probability that $$B$$
contains the prize given that Monty opened door $$C$$.

To start, we will utilize an implicit assumption that Monty necessarily
will reveal a goat when the game is played. This assumption is minimal, and
in particular imposes no repeatability constraints.

By Bayes' rule:

$$\begin{align*}
\mathbb P(B \text{ has prize} \mid C \text{ opened})
&= \frac{\mathbb P(B \text{ has prize}) \mathbb P(C \text{ opened} \mid B \text{ has prize})}
{\mathbb P( C \text{ opened})} \\
&= \frac{(1/3)(1)}{(1/2)} \\
&= 2/3.
\end{align*}$$

This of course implies that $$\mathbb P( A \text{ has prize} \mid C \text{
opened} ) =1/3$$. This proves that a contestant is twice as likely to win the
prize when they chose to open the door opposite of their original choice.


# Generalization and Abstraction

The [Bayesian](#bayesian-updates) approach suggests a new intuition. When
the contestant opts to switch doors they are
actually betting that their initial selection did not contain the prize.
To formalize this intuition we consider a generalization of the Monty Hall
Problem that removes the implicit assumption used in the Bayesian approach above.

Let $$x$$ be an element chosen uniformly at random from a finite set $$X$$.
Moreover, let $$A$$ denote some random subset of $$X$$.
Suppose that we learn that $$x \notin B \subset A$$. 

$$
P(x \in A | x \notin B \subset A) = P(x \in A)P(x \notin B | x \in A)/P(x \notin B)
$$

This doesn't change
the fact that $$ \mathbb P(x \in A)

$$x$$, $$y$$ be elements selected uniformly with replacement from $$X$$.
We learn that $$ x
Furthermore, set $$A  := X - \{x\}$$. 

Suppose $$B$$ is a subset of $$X$$ of size $$m$$ that does not contain
$$x$$.  We learn that $$y \notin B$$. What's the probability that 
$$y \neq x$$?

The revelation that $$y \notin A$$

It's clear that initially $$\mathbb P(y \neq x) = (n-1)/n$$.

