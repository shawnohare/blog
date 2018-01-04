+++
title = "All Horses Are the Same Color"
date = 2013-03-29T16:32:00Z
updated = 2013-03-30T12:27:15Z
categories= ["math"]
tags = ["proof"]
markup = "mmark"
blogimport = true 
math = true

+++


I was fortunate to TA UCSC's introductory proofs course three times.  One of the exercises I like to pose to my students is the following fallacious induction proof that all horses are the same color.

<b>The "Proof"</b>

As a base case, it's clear that any horse is the same color as itself.  Assume as an inductive hypothesis that any collection of n horses are the same color, where n is some fixed natural number.  Given any collection of n+1 horses, we may select a subset consisting of all but a single horse.  By the inductive hypothesis, all the horses in this subset are the same color.  Now regroup the horses and select another n horse subset, but this time we pick the horse that left out of the first selection.  Again all the horses in this subset are the same color, so all the horses in the original set are the same color.



<!--more-->




<b>What's wrong?</b>

A bit of thought shows that the inductive argument above only works when n+1 is at least 3, so a separate argument is necessary for the case of two horses.  Of course, one would be hard pressed to prove that any two horses are the same color as one another.  The proof presented above tries to intentionally obscure its reliance on there being sufficiently many horses.  It might be worth examining the essence of the statement and proof by way of abstraction.

<b>A generalization</b>

Really, the statement that all horses are the same color amounts to the following claim about set relations.

Proposition.  Every equivalence relation on a non-empty, finite (or indeed, inductive) set is total, i.e., there is only one equivalence class. 

This is certainly false, for if $$ A$$ is any non-empty set with at least two elements then the diagonal relation $$ \Delta(A):=\{ (a,a) \in A \times A \mid a \in A\}$$ is an equivalence relation but each equivalence class is a singleton set.  Let's examine the fallacious proof that all horses are the same color in this more general contex.

"Proof" of the Proposition.  As a base case for induction, note that any equivalence relation on a singleton set is reflexive, and hence non-empty, so is total.  Assume then that any equivalence relation on a finite set with $$ n \geq 2$$ elements is total.  Let $$ A=\{ a_1, \dots, a_{n+1} \}$$ be any set with$$ n+1$$ elements and suppose $$ R$$ is an equivalence relation on $$ A$$.  Set $$ B:=\{ a_1, \dots, a_n \}$$ and $$ C:=\{ a_2, \dots, a_{n+1} \}$$.  By the inductive hypothesis, the restrictions $$ R|_B := R \cap (B \times B)$$ and $$ R|_C := R \cap (C \times C)$$ are total relations on $$ B$$ and $$ C$$, respectively.  To conclude that $$ R$$ is total on $$ A$$ it remains to show that $$ (a_1, a_{n+1}) \in R$$.  Since $$ a_2 \in B \cap C$$, we have $$ (a_1, a_2) \in R$$ and $$ (a_2, a_{n+1}) \in R$$ so $$ (a_1, a_{n+1}) \in R$$, as desired. $$\square$$

<b>Conclusion</b>

As we can see, to relate the first element to the last element we needed an intermediate element, and so our inductive argument relies on there being at least three elements in the set.  The upshot is that it's important to establish all of your bases, so to speak.
