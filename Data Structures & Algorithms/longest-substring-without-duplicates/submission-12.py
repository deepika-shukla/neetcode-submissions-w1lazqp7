class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        longest = 0
        index = [0,0]
        l, r = 0, 0

        while r < len(s):
            
            count[s[r]] = 1 + count.get(s[r] , 0)

            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            if (r-l +1 ) > longest:
                longest = r-l+1
                index = [l,r]


            r += 1
        return longest