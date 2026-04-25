class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for l in s:
            counts[l] = counts.get(l, 0) + 1
        for l in t:
            counts[l] = counts.get(l, 0) - 1
        for c in counts.values():
            if c != 0: return False
        return True
        