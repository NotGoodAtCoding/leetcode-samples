def findDuplicate(nums: List[int]) -> int:
    exists = {}
    for n in nums:
        if exists.get(n):
            return n
        exists[n] = True
    return -1


# I looked it up

# def findDuplicate(nums: List[int]) -> int:
#     fast = slow = nums[0]
#     while True:
#         fast = nums[nums[fast]]
#         slow = nums[slow]
#
#         if fast == slow:
#             break
#
#     fast = nums[0]
#
#     while fast != slow:
#         fast = nums[fast]
#         slow = nums[slow]
#
#     return fast
