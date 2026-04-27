class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for i in range(len(nums) + 1)]
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        for n, c in counts.items():
            freqs[c].append(n)
        topK = []
        pointer = len(nums)
        while len(topK) != k:
            topK += freqs[pointer]
            pointer -= 1
        return topK
