+++
title = "TF-IDF for Document Clustering"
date = 2013-12-10T19:56:00Z
categories = ["data science"]
groups = ["nlp", "clustering"]
tags = ["tf-idf"]
blogimport = true 
notoc = true
+++

In this post we discuss a standard way to encode a text document as a vector
using a term frequency-inverse document frequency (tf-idf) score for each 
word,  with an aim to cluster similar documents in a corpus.

<!--more-->

Suppose we have a corpus of text documents $\mathcal D$.
Each document $D$ in the set $\mathcal D$ is a bag (multiset) of words.
We would like to create a metric on $\mathcal D$ that gives the similarity 
between two documents.  One approach is to embed $\mathcal D$ into some
high dimensional Euclidean space $\mathbb R^n$ and take the usual 
Euclidean metric.   This embedding 
$\mathbf v \colon \mathcal D \to \mathbb R^n$  maps a document $D$ to
some vector $\mathbf v(D)$ in $\mathbb R^n$.
We call the resulting vector $\mathbf v(D)$ the vectorization of $D$.  

It's useful to preprocess the documents in the corpus.
For each document $D$ we remove certain stop words---words that appear in
nearly all texts. Some examples would be: most, the, it, be, in, etc.
Once the stop words are removed, we want to stem each word in $D$ so that
different forms of the same word are not treated as separate words.
For instance, we want to regard "go" and "going" as the same word.

Assume now that each document in the corpus has gone through this preprocessing step.
We can obtain the corpus vocabulary $\mathcal V$---the set of all distinct
words that appear in the corpus---by taking the union over $\mathcal D$.  
That is, 

\\[   
  \mathcal V := \bigcup \limits_{D \in \mathcal D} D. 
\\] 

Since $\mathcal V$ is a set, all duplicate words are ignored.
We can now naively embed $\mathcal D$ into the $\mathbb R$-span of 
$\mathcal V$ via $D \mapsto \sum_{w \in \mathcal D} w$.
This simply counts the number of times each word $w \in \mathcal V$ appears 
in $\mathcal D$.  To conserve memory we can record only sparse vectors if we so desire.
This naive approach has one immediate problem.
The documents $D_1$, $D_2$ consisting of {"Whale."} and {"Whale. Whale."}
have a distance of $2$ in $\mathbb R \mathcal V$ despite the fact they
contain the same content, more or less.
To address this we could of course normalize each vectorized document,
but this presents problems.  Certain words might appear in a lot of documents,
but do so in high frequency in a particular subset of related documents.
Additionally, some words might appear in every single document.
These words are completely superfluous for clustering.

To take these factors into account, we should weight each word in a 
document by how frequently it appears in said document (term frequency) 
and also by how infrequently it occurs in the entire corpus 
(inverse document frequency).

First define the raw count function 

\\[  
f \colon \mathcal V \times \mathcal D \to \mathbb Z 
\\]

where $f(w,D)$ is the number of times the word $w$ appears in the document $D$.
Viewing $D$ as a subset of $\mathcal V$, let $\chi_D \colon \mathcal V \to \{ 0, 1\}$ 
denote the indicator function for $ D$.  
That is, 

\\[  
   \chi_D(w) = 
   \begin{cases}   
     1 & \text{if $w \in D$,} \\\\   
     0 & \text{if $w \notin D$.}  
   \end{cases} 
\\] 

For a real number $k \in [0,1]$, the $k$-augmented term frequency 
function is 

\\[  
  tf_k \colon \mathcal V \times \mathcal D \to \mathbb R,
  \quad  (w,D) \mapsto k \cdot \chi_D(w) +  
  \frac{(1-k) f(w,D)}{ \max \left\\{ f(v,D) \mid v \in D \right\\}}.
\\] 

Typically $k=0.5$. In this case, a word receives a weight of $0.5$ if it 
appears in the document at all an an additional weight for how frequently 
it occurs.  This added weight takes into the account the fact that longer 
documents tend to have higher general word frequencies. 
Now define the inverse-document-frequency by 

\\[  
  idf \colon \mathcal V  \to \mathbb R,
  \quad   w \mapsto \log \left(  \frac{|\mathcal D|}{| \\{ E \in \mathcal D \mid w \in E \\}|} \right). 
\\] 

Note that if $w$ appears in each document then $idf(w)=\log 1 = 0$.
If $w$ appears in $10$ documents and there are a hundred total documents, then $idf(w)=1$.
If there were a thousand total documents then $idf(w)=2$.  

The desired embedding of $\mathcal D$ into $\mathbb R \mathcal V$ is 
\\[  
  \mathbf v \colon \mathcal D \to \mathbb R \mathcal V,
  \quad  D \mapsto \sum _{\substack{ w \in \mathcal V
  \land w \in D}} (tf_k (w,D) \cdot idf(w,D)) \cdot w 
\\] 

Now $\mathbf v( \mathcal D)$ is a subset of $\mathbb R \mathcal V$,
and we can cluster the documents using any technique that works well in a 
high-dimensional Euclidean space.   
