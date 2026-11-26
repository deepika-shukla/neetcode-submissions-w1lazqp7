class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        l = 0
        s = 0
        found = 0

        for r in range(len(nums)):
            if (r-l+1) > k:
                s -= nums[l]
                l += 1
            
            s += nums[r]
            if r - l + 1 == k and s >= threshold * k:
                found += 1
        return found
        