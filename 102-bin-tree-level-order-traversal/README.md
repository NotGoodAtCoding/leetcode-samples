Task is to transform the representation of the tree as a level-order representation. Tree nodes lend themselves well to this traversal due to access to left/right without further traversal of the tree.

Answer is order-dependent on the dfs implementation by adding the left child before the right child to the final representation based on the height / depth of the tree at the point being traversed.

As the dfs runs and populates the Level Order Traversal (LOT):

```
Tree:
   1
 2   3
4 5 6 7

LOT:
1: [ [1] ]
2: [ [1], [2] ]
3: [ [1], [2],    [4] ]
4: [ [1], [2],    [4, 5] ]
5: [ [1], [2, 3], [4, 5] ]
6: [ [1], [2, 3], [4, 5, 6] ]
7: [ [1], [2, 3], [4, 5, 6, 7] ]

```


A BFS implementation may be easier to reason about - TODO: Add a bfs implementation to this problem. 
