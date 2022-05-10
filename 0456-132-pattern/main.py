def find132pattern(nums: List[int]) -> bool:
    s = []  #tuple[int, int] (num, runningMinimum), monotonic decreasing
    curMin = nums[0]

    for n in nums[1:]:
        while s and n >= s[-1][0]:
            s.pop()
        if s and n > s[-1][1]:
            return True

        s.append((n, curMin))
        curMin = min(curMin, n)
    return False
