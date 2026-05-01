class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(32):
            digit = n & 1
            rev += digit << (31-i) 
            n = n >> 1
        return rev