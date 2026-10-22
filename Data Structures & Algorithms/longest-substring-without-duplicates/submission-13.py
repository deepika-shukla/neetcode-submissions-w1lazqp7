class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = {}
        m = 0
        r = 0
        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)

            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            if m < (r-l+1):
                m = r-l+1
            r += 1
        return m