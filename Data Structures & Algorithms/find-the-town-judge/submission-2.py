class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {}

        for k,v in trust:
            d[k] = v
        
        for i in range(1, n+1):
            if i not in d:
                for k,v in d.items():
                    if v != i:
                        return -1
                return i
        return -1