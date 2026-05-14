class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        res = 1

        for i in range(n):
            mini = maxi = nums[i]
            for j in range(i + 1, n):
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[j])
                if maxi - mini > limit:
                    break
                res = max(res, j - i + 1)

        return res