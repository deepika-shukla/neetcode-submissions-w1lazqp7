class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force we traverse the array to find next max
        output = []
        
        for i in range(len(temperatures)):
            found = False
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    output.append(j-i)
                    found = True
                    break
            if not found:
                output.append(0)
        return output