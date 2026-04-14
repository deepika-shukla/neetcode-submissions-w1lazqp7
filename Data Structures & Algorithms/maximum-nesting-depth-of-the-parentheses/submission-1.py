class Solution:
    def maxDepth(self, s: str) -> int:
        c = 0
        m = 0
        for i in s:
            if m < c:
                m = c
            if i == "(":
                c += 1
            elif i == ")":
                c -= 1
        return m
