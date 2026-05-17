class Solution:
    def isValid(self, s: str) -> bool:
        match = { "]" : "[", "}" : "{", ")" : "("}
        stack = []

        for i in s:
            if i == "[" or i == "{" or i == "(":
                stack.append(i)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if val != match[i]:
                    return False
        return len(stack) == 0