class Solution:
    def reverseBits(self, n: int) -> int:
        rev= 0
        for i in range(32):
            bit = n >> i & 1 # we will get bit
            rev = rev | bit << (31 - i) # get that bit at corerct position

        return rev