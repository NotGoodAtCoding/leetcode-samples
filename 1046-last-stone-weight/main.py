import heapq
class Solution:
    # create a max heap
    # pop the largest two, take the diff, and push back onto the heap
    # stop when heap size <=1
    # we can invert the values to reverse the sort order of the heap
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneheap = [-weight for weight in stones]
        heapq.heapify(stoneheap)

        while len(stones) > 1:
            stone1 = heapq.heappop(a)
            stone2 = heapq.heappop(a)
            remainder = stone1 - stone2
            if remainder:
                heapq.heappush(remainder)
        return -stoneheap[0] if stoneheap else 0
