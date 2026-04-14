class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        c = 0
        m = 0
        for i in s:
            if m < c:
                m = c
            if i == "(":
                stack.append("(")
                c += 1
            elif i == ")":
                stack.pop()
                c -= 1
        return m
