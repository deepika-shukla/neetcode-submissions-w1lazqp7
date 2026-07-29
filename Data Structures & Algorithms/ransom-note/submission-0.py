class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = {}
        d2 = {}
        for i in ransomNote:
            d1[i] = 1 + d1.get(i,0)
        for j in magazine:
            d2[j] = 1 + d2.get(j,0)

        for i in ransomNote:
            if i in d2 and d2[i] >= d1[i]:
                continue
            else:
                return False
        return True