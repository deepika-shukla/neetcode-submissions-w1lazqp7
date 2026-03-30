class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if s1 == "":
            return True
        if s2 == "":
            return False
        
        # two pointers
        l = 0 
        r = 0

        # dictionary to store all charcter of s1
        s1_dic = {}
        for i in s1:
            s1_dic[i] = 1 + s1_dic.get(i, 0)
        
        #size of s1
        size = len(s1)
        
        #dic ro store s2
        s2_dic = {}

        # now we will traverse through s2
        while r < len(s2):
            s2_dic[s2[r]] = 1 + s2_dic.get(s2[r], 0)
            #check if both dic matches
            if s1_dic == s2_dic:
                return True
            if (l + r + 1) >= size:
                # remove the left side element
                if s2_dic[s2[l]] == 1:
                    del s2_dic[s2[l]]
                else:
                    s2_dic[s2[l]] -= 1
                
                l += 1
            
            r += 1
        return False


