class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_t = {}
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)
        
        for i in s:
            count_t[i] -= 1
        
        for k, v in count_t.items():
            if v >= 1:
                return k