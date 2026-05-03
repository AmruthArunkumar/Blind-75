class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = set()
        p = 0
        q = 0
        while p < len(s) and q < len(s):
            if s[q] not in window: 
                window.add(s[q])
                q += 1
            else:
                while s[q] in window:
                    window.remove(s[p])
                    p += 1
            if len(window) > longest: longest = len(window)
        return longest