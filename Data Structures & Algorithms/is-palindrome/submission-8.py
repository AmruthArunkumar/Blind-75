class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""
        for l in s:
            if l.isalnum(): c += l.lower()
        p = 0
        q = len(c) - 1
        if p >= q: return True
        while c[p] == c[q]:
            if p >= q: return True
            p += 1
            q -= 1
        return False