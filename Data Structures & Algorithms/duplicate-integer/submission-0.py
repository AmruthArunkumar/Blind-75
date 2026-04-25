class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for n in nums:
            count = counts.get(n, 0)
            if (count != 0):
                return True
            else:
                counts[n] = counts.get(n, 0) + 1
        return False