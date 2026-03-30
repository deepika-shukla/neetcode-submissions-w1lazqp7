class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        rev = 0
        while x:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10
        
        if temp == rev:
            return True
        return False