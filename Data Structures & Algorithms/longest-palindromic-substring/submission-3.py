class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        longest = ""

        for i in range(len(s)):
            # we need to find which is the maximum palidrome from here
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_len:
                    longest = s[l:r+1]
                    max_len = r-l+1
                l -= 1
                r += 1
            
            # odd length 
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_len:
                    longest = s[l:r+1]
                    max_len = r-l+1
                l -= 1
                r += 1
        return longest