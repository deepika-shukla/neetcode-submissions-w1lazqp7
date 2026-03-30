class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        l = 0
        size = 0

        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
            if size < r-l+1:
                size = r-l+1

        return size

        