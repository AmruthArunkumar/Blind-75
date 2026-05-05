class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"}": "{", ")": "(", "]": "["}
        for l in s:
            if l in "{[(":
                stack.append(l)
            else:
                if not stack:
                    return False
                elif stack[-1] != pairs[l]:
                    return False
                else:
                    stack.pop(-1)
        if len(stack) == 0: return True
        return False