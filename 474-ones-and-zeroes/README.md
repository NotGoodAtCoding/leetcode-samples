I visualized this problem as a kind of path optimization problem using BFS, or a "sum of vectors in a bounded context" although it can also be visualized as a knapsack problem with two different "weight" components.

The optimal "path" is one that hits the most nodes while remaining in the bounds.

We consider a 2-d Euclidean space. A standard x-y plane, if we don't want to be pretentious. The "x" axis is the number of 0s, and the "y" axis is the number of 1s. `(x,y) => (0s, 1s)`

```
# bounds : 5 1's and 4 0's

5 |________
4 |       |
3 |       |
2 |       |
1 |       |
0 ___________
  0 1 2 3 4 5

# now visualize the given strs as denoting the magnitude of each component vector
# V = (Vx, Vy), or Vx + Vy

# ex. see (3,3) and (4,1) to the best graphical capabilities of markdown
5 |
4 |
3 |  /
2 | /
1 |/_,---''
0 ___________
  0 1 2 3 4 5

# Let's visualize a path
# for the sake of clarity I'll use only vertical/horizontal/45* paths
# and we have something like the strs
# [ 0, 1, 10, 11, 00]
6 |
5 |    __   (11)
4 |   |     (00)
3 |  _|     (1)
2 | |    (0)
1 |/   (10)
0 ________________
  0 1 2 3 4 5 6 7 8
# and we keep in mind that the total vector is (3,4) and it does not matter what order the vectors are summed.
# this will hold true for subpaths / subsums of vectors
```

This way of viewing the problem is very practical, because now we can use properties of vectors to automatically optimize our solution. Namely, the associative property of vector addition. So we know that for vectors `a, b : a + b == b + a` and in the context of our problem, that means that when determining paths, we do not have to worry about order.

So, let's see how this way of framing the problem helps us optimize the solution. We take a simple sample input `[01, 1, 0]` and convert it into our vectors : `(1,1), (0,1) (1,0)` (I realize that having a bunch of 1s and 0s in the input as well as the conversion to vectors is confusing...) and then we iterate over our list, adding each vector to both the origin and the HEAD of each existing vector (visited point) on our plane as we go, and putting the length of the path on each point that we hit:

```
# add (1,1)
2|
 |
1|   /
 |  /
   _______
   0   1   2

 # add (0,1)
2|    |
 |    |
1| | /
 | |/
   _______
   0   1   2


 # add (0,1)
  |      ___
 2|     |
  |  ___|___
 1| | /
  | |/___
    _______
    0   1   2

```

Two interesting things happened:
1. two paths intersected at (1,1)
2. paths are now "overlapping"

We investigate 1 first. Previously, v(1,1) updated p(1,1) to have a path length of 1, but when we add v(0,1) and v(0,2) we update that value to be 2 since we "found a better way" to reach that point with the vectors we have.

Then we address 2. Initially, this may seem to be a problem, since it implies that we could just keep going on these vector paths that we create and get a longer path than is actually possible. We take the point (2,1) on the graph - it looks like we can get to it with both `(1,1) + (1,0)` and `(1,0) + (1,0) + (0,1)`, but the way we store values on the points is stateful to the way that the path was traversed to get to the point itself, not by evaluating/traversing the connected graph of all paths again. Or, put more simply (and in the implementation of the algorithm) *each iteration tracks the depth of the path.* Since we are using a BFS, we know and update each point with the path length as being equal to the number of vectors we have added so far. The state of the graph shows that the only way to get to p(2,1) is by using 2 vectors.

Adding bounds to this is a simple value comparison of the components of the calculated vector path to the limits m, n. If, when trying to add a new vector to the graph of paths, omit invalid paths.

## Code walkthrough

```
def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

    # We track valid paths only by the information we need
    # the point (x,y), and the longest path to get there
    paths = {(0,0): 0}
    # for a minor optimization,
    longest_path = 0

    for s in strs:
        # can't update something you are iterating over
        update_paths = {}
        for point, val in paths.items():
            # convert str to vector
            vec = (s.count("0"), s.count("1"))

            # create candidate path
            vec_path = (vec[0] + point[0], vec[1] + point[1])

            # discard path if not in bounds
            if (vec_path[0] > m) or (vec_path[1] > n):
                continue

            # check if we found a more optimal path (or are creating a new path)
            if paths.get(vec_path, 0) < val +1:
                update_paths[vec_path] = val +1
                if val +1 > longest_path:
                    # if we found a new longest path, update that value
                    longest_path = val+1


        # update out of iteration
        paths.update(update_paths)

    return longest_path
```

## Further optimization

While using a map of {point : longest_path_length} was helpful for the visualization, it's not the most efficient in space or time. Instead, we can use a set of tuples like `{ ("number of 0s", "number of 1s", "longest path to this point" ) }`

So the solution (added to the code as well) looks like this:

```
def findMaxForm(self, strs: List[str], m: int, n: int):

    paths = {(0, 0, 0)}
    for s in strs:
        sm = s.count("0")
        sn = s.count("1")
        # the e means existing path
        paths |= {(length+1, sm+em, sn+en) for i, em, en in paths if sm+em<=m and sn+en<=n}
      return max(path_length for path_length, _, _ in paths)
```

But, I mean, that's not very readable...
