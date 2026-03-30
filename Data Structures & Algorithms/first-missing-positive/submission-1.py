class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        max_n = abs(max(nums))

        for i in range(1, max_n + 2):
            if i not in nums:
                return i
            