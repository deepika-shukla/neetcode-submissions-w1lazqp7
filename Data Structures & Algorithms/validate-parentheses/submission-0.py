class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")" : "(", "}" : "{", "]" : "["}

        stack = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if val != dic[i]:
                    return False
        return not stack