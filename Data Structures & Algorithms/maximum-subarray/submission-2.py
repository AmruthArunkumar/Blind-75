class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i, j = 0, 0
        maximum = nums[0]
        curr = 0
        while j < len(nums) and i < len(nums):
            curr += nums[j]
            maximum = max(maximum, curr)
            if curr <= 0:
                i = j + 1
                j += 1
                curr = 0
            else:
                j += 1
        return maximum
        