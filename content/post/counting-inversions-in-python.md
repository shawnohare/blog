---
blogimport: true
date: 2013-08-19T20:26:00Z
markup: mmark
math: true
title: Counting Inversions in Python
updated: 2015-02-03T18:44:51Z
slug: ff4465ed-549e-4ff4-a095-ff258f923605

---

Below is an O(n log(n)) algorithm for counting the number of inversions in an array of distinct positive integers.  We call the index pair (i,j) of an array A an inversion provided that i < j and A[i] > A[j].  The idea is to break the array A into a left half L:=A[:n] and a right half R:=A[:n] and then count the number of inversions in L, in R, and the number of split inversions (i,j) where i is less than n and j is greater than or equal to n.  If L and R are already sorted then we can easily count the number of split inversions via a slight augmentation to the merge subroutine of merge-sort.    


<pre class="prettyprint">def SortCount(A):
   l = len(A)
   if l > 1:
      n = l//2
      C = A[:n]
      D = A[n:]
      C, c = SortCount(A[:n])
      D, d = SortCount(A[n:])
      B, b = MergeCount(C,D)
      return B, b+c+d
   else:
      return A, 0


def MergeCount(A,B):
   count = 0
   M = []
   while A and B:
      if A[0] <= B[0]: 
         M.append(A.pop(0)) 
      else: 
         count += len(A)
         M.append(B.pop(0)) 
   M  += A + B     
   return M, count 
</pre>
