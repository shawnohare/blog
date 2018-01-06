---
blogimport: true
date: 2013-10-11T17:59:00Z
markup: mmark
math: true
tags:
- statistics
title: Linear Models
updated: 2013-10-11T18:04:07Z
slug: f2a88cf3-334d-4ad2-b572-9be51bfd57f9

---

Suppose we think that a random variable $$Y$$ (the response) is linearly dependent on random variables $$X_1, \dots, X_p$$, where $$p$$ is some integer.    We can model this by assuming that 

$$\begin{equation*}
  Y =\underbrace{ \beta_0 + \sum_{j=1}^p \beta_j X_j}_{\widehat Y} + \epsilon,  
\end{equation*}$$

 where $$\beta = (\beta_0, \dots, \beta_p)$$ is the parameter vector for said model and $$\epsilon$$ is a distribution for the residual error between the true value of $$Y$$ and the linear prediction $$\widehat Y$$.  We assume that $$\epsilon$$ has mean $$0$$. Letting $$\mathbf x$$ denote the random vector $$(1,X_1, \dots, X_p)$$, this model can be rewritten 

$$\begin{equation*}
  Y = \mathbf x \cdot \beta + \epsilon,   \quad \text{or} \quad   y(\mathbf x ) = \mathbf x \cdot \beta + \epsilon, 
\end{equation*}$$

 where $$- \cdot -$$ represents the standard inner product on $$\mathbb R^{p+1}$$.    One often assumes, as we do now, that $$\epsilon$$ has a Gaussian distribution.  The probability density function $$p$$ for $$Y$$ then becomes 

$$\begin{equation*}
  p(y \mid \mathbf x, \beta) = \mathcal N(y \mid \mu (\mathbf x), \sigma^2 (\mathbf x)) 
\end{equation*}$$

 where $$\mu(\mathbf x)  = \mathbf x \cdot \beta$$.  We will assume that the variance $$\sigma^2(\mathbf x)$$ is a constant $$\sigma^2$$.   Suppose we make the $$N$$ observations that $$Y = y^{(i)}$$ when $$X_j = x^{(i)}_j$$ for $$j=1, \dots, p$$ and $$i = 1, \dots, N$$.  Let $$\mathbf x^{(i)}$$ denote the $$i$$th feature vector.  Further, let $$\mathbf y:=(y^{(1)}, \dots, y^{(N)})$$ denote the vector of responses.  For mathematical convenience we assume that each feature vector $$\mathbf x^{(i)}$$ is a $$p+1$$-vector with first entry equal to $$1$$.   Finally, let $$\mathbf X$$ denote the $$N \times (p+1)$$ feature matrix whose $$i$$th row is just the feature vector $$\mathbf x^{(i)}$$.     Given the data above, how can we find $$\beta$$ such that $$\widehat Y$$ is best fit, in some sense? One standard way to do this is to minimize the residual sum square error 

$$\begin{equation*}
  \text{RSS}(\beta) := \| \mathbf y - \mathbf X \beta \|^2   =(\mathbf y - \mathbf X \beta ) \cdot ( \mathbf y - \mathbf X \beta )   = \sum_{i=1}^N ( y^{(i)} - \mathbf x^{(i)} \cdot \beta)^2. 
\end{equation*}$$

 Here $$\mathbf X \beta$$ denotes the usual matrix multiplication.  We can find all minimums in the usual analytical way by computing the partials of $$\text{RSS}(\beta)$$ with respect to the variables $$\beta_j$$ for $$j=0, \dots, p$$.  Letting $$\mathbf X_j$$ denote the $$j$$th column of $$\mathbf X$$, we see that 

$$\begin{align*}
  \frac{\partial \text{RSS}}{\partial \beta_j} & = 2 \sum_{i=1}^N ( y^{(i)} - \beta_j x^{(i)}_j) x^{(i)}_j \\  &= 2 (\mathbf y - \beta_j \mathbf X_j) \cdot \mathbf X_j 
\end{align*}$$

 and so $$\text{RSS}(\beta)$$ is minimized when 

$$\begin{equation*}
  \mathbf X^T ( \mathbf y - \mathbf X \beta) = 0. 
\end{equation*}$$

 In the case that $$\mathbf X^T \mathbf X$$ is not singular the unique solution is 

$$\begin{equation*}
  \widehat \beta =  (\mathbf X^T \mathbf X)^{-1} \mathbf X^T \mathbf y. 
\end{equation*}$$

 



<!--more-->



Assuming that the observed data is independently and identically distributed,  the log-likelihood function for the given data $$ \mathcal D := \{ \mathbf y, \mathbf X \}$$ is 

$$\begin{align*}
\label{eq:likelihood}  \ell (\beta) &:= \ln p (\mathcal D \mid \beta) \\    &= \sum_{i=1}^N \ln p(y^{(i)} \mid x^{(i)} , \beta) \\     &= \sum_{i=1}^{N} \ln \left[ \frac{1}{\sqrt{2 \pi \sigma^2}} \exp \left( - \frac{1}{2 \sigma^2} (y^{(i)}  - \mathbf x^{(i)} \cdot \beta)^2 \right ) \right] . 
\end{align*}$$

 It is easy to see that $$\widehat \beta$$ is a maximum likelihood estimate for the data, i.e., $$\widehat \beta$$ satisfies 

$$\begin{equation*}
  \widehat \beta = \arg \max_{\beta} \ell (\beta).  
\end{equation*}$$

 We can in turn of course suppose that the data $$\mathcal D$$ varies and consider the maximum likelihood estimator $$\widehat \beta( \mathcal D)$$, which is a random variable itself. The variance-covariance matrix for the maximum likelihood estimator $$\widehat \beta$$ is: 

$$\begin{equation*}
  \text{Var}(\widehat \beta) = (\mathbf X^T \mathbf X)^{-1} \sigma^2. 
\end{equation*}$$

   We can estimate $$\sigma^2$$ by 

$$\begin{equation*}
  \widehat \sigma^2 = \frac{1}{N-p-1} \sum_{i=1}^N (y^{(i)} - \widehat y^{(i)})^2, 
\end{equation*}$$

  where $$ \widehat y^{(i)} := \mathbf x^{(i)} \cdot \widehat \beta$$ is the response prediction of the best fit linear model. This is an unbiased estimator for $$\sigma^2$$, which means that the expectation $$E (\widehat \sigma^2) = \sigma^2$$.  
