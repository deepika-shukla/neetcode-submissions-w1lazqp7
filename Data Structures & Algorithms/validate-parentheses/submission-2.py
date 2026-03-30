class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = { '{' : '}', '[' : ']', '(': ')'}

        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if mappings[val] != i:
                    return False

        return len(stack) == 0 
        