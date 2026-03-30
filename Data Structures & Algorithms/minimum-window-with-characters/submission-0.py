class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        if len(t) > len(s):
            return ""
        
        l = 0
        window, count = {}, {}
        for i in t:
            count[i] = 1 + count.get(i,0)

        resindex, res = [0,0], 100000

        have, need = 0 ,len(count)

        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c,0)

            if c in count and window[c] == count[c]:
                have += 1
            
            while have == need:

                if (r-l+1) < res:
                    resindex = [l,r]
                    res = r-l+1
                window[s[l]] -= 1

                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1

                l += 1
        l,r = resindex

        return s[l : r + 1] if res != 100000  else ""

