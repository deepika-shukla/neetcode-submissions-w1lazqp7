class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t =="":
            return ""

        window, count = {}, {}

        for i in t:
            count[i] = 1 + count.get(i,0)
        have, need = 0, len(count)

        l=0

        res = 10000
        resindex = [0,0]

        for r in range(len(s)):
            c = s[r]

            #add in window
            window[c] = 1 + window.get(c,0)

            #check if count matches in count
            if c in count and window[c] == count[c]:
                have +=1

            #if they are equal
            while have == need:
                if (r-l + 1) < res:
                    resindex = [l,r]
                    res = r-l+1
                window[s[l]] -= 1
                
                if s[l] in count and count[s[l]] > window[s[l]]:
                    have -=1

                #reduce size 
                l += 1 
        l, r = resindex
        return s[l:r+1] if res != 10000 else ""
        