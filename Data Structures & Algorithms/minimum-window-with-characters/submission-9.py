class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge cases
        if len(t) > len(s):
            return ""
        if t == "":
            return ""
        if s == "":
            return ""
        
        l, r = 0, 0
        have, need = 0, 0
        count_s, count_t  = {}, {}

        index = [-1,-1]
        min_len = 99999999
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)
        need = len(count_t)

        while r < len(s):
            count_s[s[r]] = 1 + count_s.get(s[r], 0)
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:  # Fix 3: only update if smaller
                    min_len = r - l + 1
                    index = [l, r]
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1 
                l += 1
            r += 1
        l, r = index
        return "" if index == [-1,-1] else s[l:r+1] 


