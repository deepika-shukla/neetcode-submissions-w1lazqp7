class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {} #letter : count

        l, r = 0,0 
        count = 0
        cur = 0 

        while r < len(s):
            if s[r] in dic:
                while dic[s[r]] >= 1:
                    dic[s[l]] -= 1
                    l += 1
                    cur -= 1
            dic[s[r]] = 1 + dic.get(s[r], 0)
            cur += 1
            if cur > count:
                count = cur
            r += 1
        return count