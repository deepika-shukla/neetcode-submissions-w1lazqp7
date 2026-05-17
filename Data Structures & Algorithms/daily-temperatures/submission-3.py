class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = [] # (temperature, index)

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = i - index
            stack.append((t,i))
        
        return result