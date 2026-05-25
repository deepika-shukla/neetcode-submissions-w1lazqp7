class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # we need to find increasing subsequence
        # we can find for each index
        dp = [1] * len(nums) # each number is itself subsequence

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)