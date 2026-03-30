class Solution:
    def isValid(self, s: str) -> bool:
        pair = { ')':'(', '}':'{', ']':'['}

        stack = []

        for i in s:
            if i in "{[(":
                stack.append(i)
            else:
                if not stack:
                    return False
                b = stack.pop()
                if pair[i] != b:
                    return False
        return len(stack) == 0
