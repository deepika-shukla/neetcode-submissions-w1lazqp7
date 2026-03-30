class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # we need to find the maximum subarray
        # we can be greedy by skipping the negative sum

        cursum = 0
        max_sum = nums[0]

        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum += n
            max_sum = max(max_sum, cursum)

        return max_sum