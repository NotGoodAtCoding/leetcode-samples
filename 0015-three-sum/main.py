class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        ans = []
        for idx, num in enumerate(s_nums):
            if idx > 0 and s_nums[idx] == s_nums[idx-1]:  # skip candidates already evaluated
                continue
            start, end = idx+1, len(s_nums)-1  # see two sum ii
            while start < end:
                if s_nums[start] + s_nums[end] == -num:
                    ans.append([num, s_nums[start], s_nums[end]])
                    start += 1
                    while s_nums[start] == s_nums[start-1] and start < end:  # skip sub-candidates already evaluated
                        start +=1
                elif s_nums[start] + s_nums[end] > -num:
                    end -= 1
                else:
                    start += 1
        return ans
