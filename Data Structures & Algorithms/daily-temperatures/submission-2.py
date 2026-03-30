class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)

        #bruteforce solution : O(n^2)

        # for l in range(len(temperatures)):
        #     r = l + 1
        #     while r < len(temperatures):
        #         if temperatures[r] > temperatures[l]:
        #             result[l] = r-l
        #             break
        #         r += 1
        # return result

        ## Now usisng stack

        stack = []

        #we can store the temperature in stack unless we don't get higher
        #value than that

        for i in range(len(temperatures)): # 3
            while stack and stack[-1][1] < temperatures[i]:
                l, t = stack.pop() 
                result[l] = i - l
            stack.append([i, temperatures[i]]) # 1,38 3,36  
        
        return result
