class Solution:
    def isValid(self, s: str) -> bool:
        pair = { "}" : "{", ")" : "(", "]" : "["}
        stack = []
        for i in s:
            if i == "[" or i == "(" or i == "{":
                stack.append(i)
            else:
                if not stack:
                    return False
                b = stack.pop()
                if b != pair[i]:
                    return False
        return len(stack) == 0


