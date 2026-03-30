class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we need to find minimum substring
        # we can use sliding window technique
        # we can first have how many letters we need
        # also we need to keep track of count of letters
        if len(t) > len(s):
            return ""
        if t =="":
            return ""
        have, need = 0 , 0

        count_s, count_t  = {}, {}

        for i in t:
            count_t[i] = 1 + count_t.get(i,0)

        need = len(count_t)
        res = [-1,-1] #which will be start/end indices
        reslen = 9999999999999999

        l=0

        for r in range(len(s)):
            c = s[r]

            count_s[c] = 1 + count_s.get(c,0)
            if c in count_t and count_t[c] == count_s[c]:
                have +=1

            while have == need:
                if (r-l+1) < reslen:
                    res =  [l,r]
                    reslen = r-l+1
                count_s[s[l]] -= 1
                if s[l] in count_t and count_t[s[l]] > count_s[s[l]]:
                    have -=1

                l+=1
        l,r = res
        if reslen == 9999999999999999:
            return ""
        return s[l:r+1]



        