class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        maximum = nums[0]
        curr = 0
        while i < len(nums):
            curr += nums[i]
            maximum = max(maximum, curr)
            if curr <= 0:
                curr = 0
            i += 1
        return maximum
        