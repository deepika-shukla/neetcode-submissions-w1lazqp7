class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for n in operations:
            if n == "+":
                a, b = stack[-1], stack[-2]
                stack.append(a+b)
            elif n == "C":
                stack.pop()
            elif n == "D":
                a = stack[-1]
                stack.append(2*a)
            else:
                stack.append(int(n))
        return sum(stack)