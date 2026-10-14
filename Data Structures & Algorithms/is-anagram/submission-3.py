class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False
        # # with sorting
        # return sorted(s) == sorted(t)

        # with hashmap
        s1 = {}
        t1 = {}
        for i in range(len(s)):
            s1[s[i]] = 1 + s1.get(s[i], 0)
            t1[t[i]] = 1 + t1.get(t[i], 0)
        return s1 == t1

