class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # store key and value

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and stack[-1][0] < t:
                t_s, i_s = stack.pop()
                result[i_s] = i - i_s            
            stack.append([t,i])

        return result
