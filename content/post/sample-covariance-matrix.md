---
blogimport: true
date: 2013-10-15T15:54:00Z
markup: mmark
math: true
tags:
- statistics
title: Sample Covariance Matrix
updated: 2013-12-06T06:59:47Z
slug: 6e1ecf39-cf3c-459f-b4bd-74551fcba229

---

Suppose $$X_1, \dots, X_p$$ are random variables and $$X:=(X_1, \dots, X_p)$$ is the random vector of said random variables.  Given a sample $$\mathbf x_1, \dots \mathbf x_N$$ of $$X$$, how do we obtain an estimate for the covariance matrix $$\text{Cov}(X)$$?  <br><br> To this end, let $$\mathbf X=( \mathbf X_{ij})$$ denote the $$N \times p$$ data matrix whose $$k$$th row is $$\mathbf x_k$$ and let $$\bar x_i$$ denote the sample mean of $$X_i$$.  That is, $$\bar x_i$$ is the mean of the $$i$$th column of $$\mathbf X$$.  Then the sample covariance matrix $$Q = (Q_{ij})$$ is defined by 

$$\begin{equation*}
  Q_{ij} := \frac{1}{N-1} \sum_{k=1}^{N} (\mathbf X_{ki} - \bar x_i)(\mathbf X_{kj} - \bar x_j). 
\end{equation*}$$

 We can write this a bit more compactly if we introduce yet more notation.  Let $$\bar{\mathbf x}:=(\bar x_1, \dots, \bar x_p)$$ denote the sample mean vector and $$M$$ the $$N \times p$$ matrix with all rows equal to $$\bar{\mathbf x}$$. The matrix $$N:=\mathbf X - M$$ is the data matrix that has been centered about the sample means, and we quickly see that 

$$\begin{equation*}
  Q = N^T N. 
\end{equation*}$$


