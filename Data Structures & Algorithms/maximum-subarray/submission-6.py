class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        max_sum = nums[0]
        for i in nums:
            if s < 0:
                s = 0
            s += i
            max_sum = max(max_sum, s)
        return max_sum
