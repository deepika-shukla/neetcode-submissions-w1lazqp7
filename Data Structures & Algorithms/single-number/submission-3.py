class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0 
        for i in nums:
            n ^= i
        return n
        # because number appear twice will cancel out
        # only the single number will remain itself