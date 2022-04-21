import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # save as tuples of (dist, points)
        # chuck them in the max heap (invert distance), pop the max if above k
        # return tuple[1] for tuple in tuples

        pointheap = []

        for point in points:
            distance = -((point[0]**2 + point[1]**2) ** .5)
            if len(pointheap) == k:
                heapq.heappushpop(pointheap, (distance, point))
            else:
                heapq.heappush(pointheap, (distance, point))

        return [t[1] for t in pointheap]
