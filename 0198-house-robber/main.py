def rob(self, nums: List[int]) -> int:
    # calculate the best possible option by:
    # rob current, skip next, then get the best option from the remainder
    # skip current, rob next, then get best from the further remainder
    # skipping two is covered by us checking the case where we
    # skip current, then the best option of next is also skip current
    rob1, rob2 = 0,0
    for n in nums:
        rob2, rob1 = max(n+rob1, rob2), rob2
    return rob2
