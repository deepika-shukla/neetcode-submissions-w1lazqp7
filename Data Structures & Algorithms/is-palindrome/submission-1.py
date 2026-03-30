class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s1 = ""
        # for i in s:
        #     if i.isalnum():
        #         s1 += i.lower()
        # return s1==s1[::-1]

        #with two pointer
        l = 0
        r = len(s) - 1

        while l  < r:
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
