class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # we need to count pallindromic substrings. we can keep track
        # of each pallindromic substring from that index

        for i in range(len(s)):
            # odd
            l, r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1


            # even
            l, r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
        return count