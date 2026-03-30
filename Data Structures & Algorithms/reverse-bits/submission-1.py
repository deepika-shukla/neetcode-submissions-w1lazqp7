class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0

        for i in range(32):
            # we will find the bits in n
            bit = (n >> i) & 1
            # now we will store the bit we found in reverse
            reverse = reverse | (bit << (31 - i))
        #at the end we will get reverse
        return reverse
