class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # take l and r whose diff is equal to size of s1
        l, r = 0, len(s1) - 1
        # run a loop until r < len(s2)
        # maintain dict with character of s1

        count1 = {}
        for i in s1:
            count1[i] = 1 + count1.get(i,0)
        
        while r < len(s2):
            #maintain another dictionary
            count2 = {}
            for i in range(l, r+1):
                count2[s2[i]] = 1+count2.get(s2[i], 0)
            if count1 == count2:
                return True
            l += 1
            r += 1
        return False
        