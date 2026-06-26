class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = ""
        cur = 0
        for i in range(len(s)-1):
            l, r =  i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if cur < (r-l+1):
                    longest = s[l:r+1]
                    cur = r-l+1
                l -= 1
                r += 1
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if cur < (r-l+1):
                    longest = s[l:r+1]
                    cur = r-l+1
                l -= 1
                r += 1
        return longest
