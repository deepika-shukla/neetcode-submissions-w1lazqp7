class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # we don't want the sum of subarray to be negatice

        s = nums[0]
        cur_sum = 0
        # we need to keep track of cur_sum
        for i in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += i
            s = max(s, cur_sum)
        return s