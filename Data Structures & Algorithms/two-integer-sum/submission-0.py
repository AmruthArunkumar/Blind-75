class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        locs = {}
        for i, n in enumerate(nums):
            if locs.get(target - n, None) != None: 
                return [locs[target-n], i]
            else: 
                locs[n] = locs.get(n, i)