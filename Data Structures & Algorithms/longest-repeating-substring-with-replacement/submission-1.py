class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        p = 0
        count = {}
        maxf = 0
        for q in range(len(s)):
            count[s[q]] = 1 + count.get(s[q], 0)
            maxf = max(maxf, count[s[q]])

            while ((q-p+1) - maxf > k):
                count[s[p]] -= 1
                p += 1
            if q-p+1 > longest: longest = q-p+1
        return longest