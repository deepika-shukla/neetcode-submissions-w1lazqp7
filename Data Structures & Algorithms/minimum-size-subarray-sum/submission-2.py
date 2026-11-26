class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s = 0
        minLen = len(nums)
        found = False
        for r in range(len(nums)):
            s += nums[r]

            while s >= target:
                found = True
                minLen = min(minLen , r-l+1)
                s -= nums[l]
                l += 1
        return minLen if found else 0
