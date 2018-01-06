---
author:
  name: Shawn O'Hare
blogimport: true
date: 2013-08-06T21:51:00Z
markup: mmark
math: true
tags:
- probability
title: A Coin Tossing Game
slug: e4bd28d7-4295-4c3d-9d17-1c2223812541

---

As an example of the law of total probabilities, I'm going to explore a slightly generalized variant of an interview question I recently encountered.  
The basic scenario is to imagine two players, let's say Amanda and Bill, both of who have a weighted coin. They take turns tossing their coin and whoever obtains the first heads wins. 
Amanda's coin comes up heads with probability $$\theta$$ and Bill's with probability $$\psi$$. 
If Amanda tosses first, what's the probability she will win? 

<!--more-->



The underlying sample space $$\Omega$$ is the set of all sequences of coin tosses that result in a game ending.  
So, for instance, $$H$$, $$TH$$, and $$TTH$$ are elements of $$\Omega$$ while $$HH$$ is not.  
Clearly, any $$\omega \in \Omega$$ must start with either $$H$$, $$TH$$ or $$TT$$.  
If we let $$A_1:=\{ H\}$$, $$A_2:=\{ TH \}$$, and define $$A_3$$ to be the set of all sequences in $$\Omega$$ that begin with $$TT$$, then $$\Omega$$ is partitioned by $$A_1$$, $$A_2$$, $$A_3$$.  
Hence for any event $$A \subseteq \Omega$$, 

$$\begin{equation*}
  p(A) = \sum_{i=1}^3 p(A | A_i) p(A_i), 
\end{equation*}$$

 where $$p(A|B):=p(A \cap B)/p(B)$$ is the conditional probability of the event $$A$$ given the event $$B$$. We want to compute $$p(A)$$ where $$A$$ is the event that Amanda wins.  
Clearly $$p(A | A_1)=1$$ and $$p(A | A_2)=0$$.  
A moment's thought reveals that $$p(A | A_3)=p(A)$$, since knowing two tails were initially tossed does not  affect Amanda's chances of winning.  
Thus 

$$\begin{equation*}
  P(A) = \theta + (1-\theta)(1-\psi) P(A), 
\end{equation*}$$

 from which we can solve for $$P(A)$$ and rewrite 

$$\begin{equation*}
  P(A) = \frac{\theta}{\theta + \psi - \theta \psi}=\frac{\theta}{\theta(1-\psi) + \psi}. 
\end{equation*}$$

 
If both coins are fair, then $$P(A) = 2/3$$, demonstrating that Amanda has a significant advantage. But what if Bill's coin is heavily weighted to come up heads?  When $$\theta = .5$$ and $$\psi=.99$$,  we see $$P(A) \approx .502$$, and so Amanda still has a slight advantage of winning!  In some sense this should be intuitively clear.  
When Bill's coin is double headed Amanda will still win half the time (assuming her coin is fair).  
In general if $$\theta = .5$$, then $$P(A)=1/(1+\psi)$$, which for $$\psi \in [0,1]$$ has a minimum value of $$1/2$$ when $$\psi=1$$.  
This proves that as long as Amanda's coin is fair, she will win at least half the time! Even when Amanda's coin is weighted toward tails, she still can have decent odds.  
When $$\theta = 1/3$$ and $$\psi=1/2$$ we see $$P(A)=1/2$$. 
