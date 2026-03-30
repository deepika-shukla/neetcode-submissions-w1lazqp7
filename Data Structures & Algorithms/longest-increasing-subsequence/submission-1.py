class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_i_s = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    longest_i_s[i] = max(longest_i_s[i], 1 + longest_i_s[j])
        return max(longest_i_s)