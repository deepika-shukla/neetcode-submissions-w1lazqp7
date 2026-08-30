class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = count = 0
        for n in nums:
            if n == 0:
                max_count = max(count, max_count)
                count = 0
            else:
                count += 1
        return max(count, max_count)
        