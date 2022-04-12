def twoSum(nums: List[int], target: int) -> List[int]:
    n_sort = sorted(nums)
    p1 = 0
    p2 = len(nums) - 1
    while p1 < p2:
        if n_sort[p1] + n_sort[p2] > target:
            p2 -= 1
        elif n_sort[p1] + n_sort[p2] < target:
            p1 += 1
        else:
            first_idx = nums.index(n_sort[p1])
            second_idx = (len(nums) -1) - nums[::-1].index(n_sort[p2])
            return [first_idx, second_idx]
