# Better solution
# heapify the incoming list, then pop the smallest values to make it size k
# this guarantees that the 0th item will be the smallest in the
# maxheap limited by k and therefore the kth largest
# when adding, if the heap is not full, just add the new val
# else, if the val is smaller than the smallest, just discard
# if larger than the smallest, then pop the smallest and add the new element

# since the 0th element in the heap is the smallest, we can always return it
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = nums
        heapq.heapify(self.max_heap)

        while len(self.max_heap) > k:
            heapq.heappop(self.max_heap) # heapq pops the smallest item

    def add(self, val: int) -> int:
        if len(self.max_heap) == self.k:  # heap is full
            if val > self.max_heap[0]:  # only add if greater than the smallest value
                heapq.heappop(self.max_heap)  # pop the smallest out
                heapq.heappush(self.max_heap, val) # add the new one in
        else:  # heap has space, let 'er in
            heapq.heappush(self.max_heap, val)
        return self.max_heap[0] # 0th item will always be the smallest of the max heap, which of size k is the kth largest
