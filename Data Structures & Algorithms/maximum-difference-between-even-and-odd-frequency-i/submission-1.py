class Solution:
    def maxDifference(self, s: str) -> int:
        # to calculate max difference between odd and even
        # brute force
        # count = {}
        # for i in s:
        #     count[i] = 1 + count.get(i,0)
        
        # odd = []
        # even = []

        # for k,v in count.items():
        #     if v % 2:
        #         odd.append(v)
        #     else:
        #         even.append(v)
        # return max(odd) - min(even)

        # optimal space

        count = {}
        for i in s:
            count[i] = 1 + count.get(i,0)
        max_odd, min_even = 0, len(s)

        for k,v in count.items():
            if v % 2:
                max_odd = max(max_odd, v)
            else:
                min_even = min(min_even, v)
        return max_odd - min_even
