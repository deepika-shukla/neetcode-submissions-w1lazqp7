class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        d = {}
        max_len = 1
        i=0
        for j in range(len(s)):
            d[s[j]] = 1 + d.get(s[j], 0)
           
            while i < len(s) and d[s[j]] > 1:
                d[s[i]] -= 1
                i += 1
            
            max_len = max(max_len, j - i + 1)
            
        return max_len