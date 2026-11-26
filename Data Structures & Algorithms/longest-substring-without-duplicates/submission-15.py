class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        l=0
        letters = set()

        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l +=1
            letters.add(s[r])
            maxL = max(maxL, r-l+1)
        return maxL