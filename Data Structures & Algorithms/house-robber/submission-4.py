class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0

        for n in nums:
            temp = max(rob1+n, rob2)
            #then shift rob1, rob2 to proceeding values
            rob1 = rob2
            rob2 = temp # the max till we have now
        return rob2
