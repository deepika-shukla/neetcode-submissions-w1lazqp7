class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force we traverse the array to find next max
        # output = []
        
        # for i in range(len(temperatures)):
        #     found = False
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             output.append(j-i)
        #             found = True
        #             break
        #     if not found:
        #         output.append(0)
        # return output


        # using stack : to fill in monotanioulsy decreasing order
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > stack[-1][0]:
                val, index = stack.pop()
                output[index] = i - index
            stack.append([temperatures[i], i])
        return output
