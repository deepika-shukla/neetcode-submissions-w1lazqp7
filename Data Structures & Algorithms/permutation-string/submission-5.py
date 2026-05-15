class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge cases
        if s1 == "":
            return True
        if s2 == "":
            return False
        d1 = {}
        for i in s1:
            d1[i] = 1 + d1.get(i,0)
        d2 = {}
        l = 0
        r = 0
        while r < len(s2):
            d2[s2[r]] = 1 + d2.get(s2[r], 0)
            if d1 == d2:
                return True
            if (r+l+1) >= len(s1):
                d2[s2[l]] -= 1
                if d2[s2[l]] < 1:
                    del d2[s2[l]]
                l += 1
            r += 1
        return False


        
        