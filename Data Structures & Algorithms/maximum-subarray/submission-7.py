class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        max_sum = nums[0]

        for i in nums:
            s += i
            max_sum = max(s, max_sum)
            if s < 0:
                s = 0
            
        return max_sum