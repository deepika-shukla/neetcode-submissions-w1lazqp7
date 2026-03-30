class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [1] * len(nums)

        #reverse traversal
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    sub[i] = max(sub[i], 1 + sub[j])
        return max(sub)