class Solution:
    def reverseBits(self, n: int) -> int:
        #to everse the bit, we need to shift the 1 for each bit 
        #and do the or operation
        rev = 0
        for i in range(32):
            bit = n >> i & 1
            rev |= bit << (31 - i) 
        return rev

