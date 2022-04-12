Naive solution is combinatorially comparing all values. O(n!) is a terrible runtime.

Optimized solution is much easier to implement if the return values are the actual int values, not their indices in the original list.

Sort a copy of the incoming list. Keep original copy for later index solving.
Start at either end of the list (index 0 and index len(list)-1 ) - we'll call this head and tail
If the sum of head and tail is GREATER than value, then we need to reduce the tail to try to approach the value.
If the sum of head and tail is LESSER than value, then we need to increase the head to approach the value.
No need for out-of-bounds checking since the problem guarantees at least one solution.
If we find the solution, then we need to convert these found values back to indices. This is done by finding the HEAD starting at the beginning of the list and TAIL starting at the end of the list (hence the reverse and flip), needed to prevent index(e) from returning the first occurrence and failing the case { [3, 3] , 6 }.

Visualized run of the algorithm:

```
inputs: nums=[2,3,4,5,8,9] target = 9

 p1              p2
[ 2, 3, 4, 5, 8, 9 ]
# 2 + 9 > 9, decrement p2

 p1           p2
[ 2, 3, 4, 5, 8, 9 ]
# 2 + 8 > 9, decrement p2

 p1        p2
[ 2, 3, 4, 5, 8, 9 ]
# 2 + 5 < 9, increment p1

     p1    p2
[ 2, 3, 4, 5, 8, 9 ]
# 3 + 5 < 9, increment p1

        p1 p2
[ 2, 3, 4, 5, 8, 9 ]
# 4 + 5 = 9, convert indices and return

```

We could avoid having to check back through the list to get the indices of the solutions by instead converting the incoming List[int] to a List[tuple[int, int]] where tuple[0] is the value and tuple[1] is the original index, which should result in a slightly better real-world runtime.


This reduces the problem to O(nlogn) due to list sort being O(nlogn) while iterating once is O(n).
