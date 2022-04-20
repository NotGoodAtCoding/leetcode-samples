# naive solution
# sort incoming list O(nlogn)
# when adding, use bin search insert O(logn)
# return sorted[k]

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)[k:]
        self.k = k

    def _insert(self, val: int):
       # binary insert
       low, high = 0, len(self.nums)
       while low <= high:
           mid = low + (high - low) //2
           if mid == len(self.nums):
               break
           elif val == self.nums[mid]:
               low = mid +1
               break
           elif (val > self.nums[mid]):
               low = mid + 1
           else:
               high = mid -1

       self.nums = self.nums[:low] + [val] + self.nums[low:]

    def add(self, val: int) -> int:
        if len(self.nums) == k:
            if val > self.nums[0]:
                del self.nums[0]
                self._insert(val)
        else:
            self._insert(val)

        return self.nums[0]


# bin insert solution with limited heap to k

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        if k < len(nums):
            self.nums = self.nums[len(nums)-k:]
        self.k = k

    def _insert(self, val: int):
       # binary insert
        low, high = 0, len(self.nums)
        while low <= high:
            mid = low + (high - low) //2
            if mid == len(self.nums):
                break
            elif val == self.nums[mid]:
                low = mid +1
                break
            elif (val > self.nums[mid]):
                low = mid + 1
            else:
                high = mid -1

        self.nums = self.nums[:low] + [val] + self.nums[low:]

    def add(self, val: int) -> int:
        if len(self.nums) == self.k:
            if val > self.nums[0]:
                del self.nums[0]
                self._insert(val)
        else:
            self._insert(val)

        return self.nums[0]
