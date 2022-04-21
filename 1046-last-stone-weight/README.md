I'm starting to love heaps now that I understand them more.

The python default heap util using heapq is a little unfortunate in the rigid implementation, since in order to have the implementation act as a max heap you need to invert the values, making it confusing for ranges that encompass 0. Plus having each method on the module start with "heap*" except for merge (and nlargest/nsmallest) is a little redundant. I digress.

As hinted, it's easy to use a max heap to solve this problem, since we can efficiently pop the top two items, reduce them, and push them back onto the heap.

```
def lastStoneWeight(self, stones: List[int]) -> int:
    # negate the weights to create max heap
    # (or, rather, so that pop returns the max of the heap, not the min)
    stoneheap = [-weight for weight in stones]
    # the elusive "self commenting code"
    heapq.heapify(stoneheap)

    while len(stones) > 1:             # while at least two stones left
        stone1 = heapq.heappop(a)      # take the largest stone
        stone2 = heapq.heappop(a)      # and the second largest stone
        remainder = stone1 - stone2    # smash them
        if remainder:                  # and if there's anything left
            heapq.heappush(remainder)  # push it back on the heap

    # when done smashing, there will be either 1 stone left or nothing
    # remember that the stone weight needs to be inverted again
    return -stoneheap[0] if stoneheap else 0
```
