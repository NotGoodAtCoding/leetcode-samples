Inverting the key to turn the python default minheap into a maxheap comes in clutch. As well as python being able to deal with `sqrt` as `^(1/2)` which I was pleasantly surprised by. I was fully expecting it to only accept positive ints.

Another straightforward max heap implementation. Limit size to k.

```
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # init the heap to empty
        pointheap = []

        for point in points:
            # equals sqrt(x^2 + y^2) for point [x, y]
            # no need to take differences since we are comparing against the origin
            # if we were comparing against another point, we would take the differences to
            # get the Euclidean distance
            # here's also where we use the trick of sqrt(x) == x^(1/2)
            # then we also invert the distance to create a max heap (pop "furthest" point)
            distance = -((point[0]**2 + point[1]**2) ** .5)  

            # if the heap is full, we must evict
            if len(pointheap) == k:
                # pushpop is more efficient than subsequent calls to
                # push then pop
                heapq.heappushpop(pointheap, (distance, point))
            else:
                # if its not full, we are free to push this new point.
                heapq.heappush(pointheap, (distance, point))

        # since the heap is limited to k, we automagically have the k closest points
        # luckily order does not matter either.
        return [t[1] for t in pointheap]
```
