class Solution:
    def maxDifference(self, s: str) -> int:
        # to calculate max difference between odd and even
        # brute force
        count = {}
        for i in s:
            count[i] = 1 + count.get(i,0)
        
        odd = []
        even = []

        for k,v in count.items():
            if v % 2:
                odd.append(v)
            else:
                even.append(v)
        return max(odd) - min(even)

        