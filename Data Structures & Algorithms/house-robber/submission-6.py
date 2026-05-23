class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # rob1, rob2, continuation of nums
        # we are taking these two as we have two subproeblem
        # either rob1 + n, or skip rob1 and take rob2

        for n in nums:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2