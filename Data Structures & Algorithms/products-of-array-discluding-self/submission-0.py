class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        p = 0
        while p < len(nums):
            prefix[p] = 1 if p == 0 else prefix[p-1] * nums[p-1]
            p += 1
        p = len(nums) - 1
        while p >= 0:
            postfix[p] = 1 if p == (len(nums) - 1) else postfix[p+1] * nums[p+1]
            p -= 1
        return [x * y for x, y in zip(prefix, postfix)]