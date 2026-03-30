class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)

        #bruteforce solution

        for l in range(len(temperatures)):
            r = l + 1
            while r < len(temperatures):
                if temperatures[r] > temperatures[l]:
                    result[l] = r-l
                    break
                r += 1
        return result