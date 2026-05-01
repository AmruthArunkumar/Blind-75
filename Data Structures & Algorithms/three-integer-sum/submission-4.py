class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        p = 0
        q = 1
        r = len(nums) - 1
        while p < len(nums) and nums[p] <= 0:
            if q >= r:
                curr = nums[p]
                while p < len(nums) and nums[p] == curr: p += 1
                q = p + 1
                r = len(nums) - 1
                continue
            sum = nums[p] + nums[q] + nums[r]
            if sum == 0: 
                solutions.append([nums[p], nums[q], nums[r]])
                curr = nums[q]
                while q < len(nums) and nums[q] == curr: q += 1
                curr = nums[r]
                while r >= 0 and nums[r] == curr: r -= 1
            elif sum < 0:
                q += 1
            elif sum > 0:
                r -= 1
        return solutions