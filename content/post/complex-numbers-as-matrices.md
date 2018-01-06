---
blogimport: true
date: 2013-06-09T14:43:00Z
markup: mmark
math: true
title: Complex Numbers as Matrices
updated: 2013-06-10T10:15:43Z

slug: af8449db-b351-4ae6-a367-805ce666ee2f

---

Many people take exception with the complex number field $$\mathbb C$$ because the equality 

$$\begin{equation}
\label{eq:neg1}  i^2 = -1 
\end{equation}$$

 rankles them in some way.  I suspect that the layperson's distaste for this identity is their wont to interpret $$i$$ as a real number, since they have the most experience with the arithmetic of real numbers.  Surely our convention of calling numbers such as $$\sqrt 2$$, $$\pi$$, and $$e$$ real but $$-2i$$ "purely imaginary" doesn't help.    

Identities of the form in \eqref{eq:neg1} abound in the wild.  For instance, within the ring $$M_2(\mathbb R)$$ of $$2 \times 2$$-matrices with real entries, the rotation by $$90^{\circ}$$ matrix $$R$$ defined by 

$$\begin{equation}
\label{eq:matrix}  R := \begin{pmatrix}   0 & -1 \\   1 & 0  \end{pmatrix} 
\end{equation}$$

 satisfies $$R^2 = -\mathbf{1}$$.  Here $$\mathbf{1}$$ signifies the identity matrix 

$$\begin{equation*}
  \mathbf{1}:=\begin{pmatrix}   1 & 0 \\   0 & 1  \end{pmatrix}, 
\end{equation*}$$

 which is the multiplicative identity in $$M_2(\mathbb R)$$.    


<!--more-->



As another example, recall that two integers $$x$$ and $$y$$ are identified modulo a natural number $$n$$, written $$x = y \mod n$$, provided that there exists an integer $$s$$ such that 

$$\begin{equation*}
  x = sn + y. 
\end{equation*}$$

 Since $$2^2 = 1 \cdot 5 +  (-1)$$, we have 

$$\begin{equation*}
  2^2 = -1 \mod 5. 
\end{equation*}$$



To better understand why \eqref{eq:neg1} should cause us no philosophical consternation, let's consider how complex numbers are built. The complex number field $$\mathbb C$$ consists of elements of the form $$a + bi$$, where $$a$$ and $$b$$ are real numbers and $$i$$ is merely a symbol.  Given two complex numbers $$a + bi$$ and $$c + di$$, we add them via $$(a + bi) + (c + di):=(a + c) + (b + d)i$$ and multiply them via $$(a + bi) \cdot (c + di) := (ac-bd) + (ad + bc)i$$.  Given these definitions, $$i^2 = (0 + i) \cdot (0 + i) = -1$$.  This is actually what is meant when we say that "$$i$$ is the square root of $$-1$$".   

We can also identify a subset of $$M_2(\mathbb R)$$ that has the exact same additive and multiplicative structure as $$\mathbb C$$.  Consider the set $$\mathbb M$$ of real $$2 \times 2$$-matrices that have the form 

$$\begin{equation*}
  \begin{pmatrix}   a & -b \\   b & a  \end{pmatrix}, 
\end{equation*}$$

 where $$a$$ and $$b$$ are real numbers.  It is easy to verify that if $$A$$ and $$B$$ are two matrices in $$\mathbb M$$, then $$A+B$$ and $$AB$$ are both in $$\mathbb M$$, so $$\mathbb M$$ is closed under addition and multiplication.  Now observe that if $$a$$, $$b$$, $$c$$, $$d$$ are real numbers, then 

$$\begin{equation*}
  \begin{pmatrix}   a & -b \\   b & a  \end{pmatrix}  \begin{pmatrix}   c & -d \\   d & c  \end{pmatrix}  =  \begin{pmatrix}   ac-bd & -(ad+bc) \\   ad + bc & ac-bd  \end{pmatrix}.  
\end{equation*}$$

 This is the same multiplication law that we defined for $$\mathbb C$$.  Indeed, we can canonically identify the complex number $$a+bi$$ with the matrix 

$$\begin{equation*}
  \begin{pmatrix}   a & -b \\   b & a  \end{pmatrix}. 
\end{equation*}$$

 When $$a=0$$ and $$b=1$$ we have the complex number $$i$$, which corresponds to our rotation matrix $$R$$ from \eqref{eq:matrix}.  There are many other ways to construct an algebraic object with the same additive and multiplicative structures as the field of complex numbers.  This demonstrates to some degree that the isomorphism type of $$\mathbb C$$, i.e., the algebraic structure of $$\mathbb C$$ viewed without regard to what the elements represent, is quite a natural object. 
