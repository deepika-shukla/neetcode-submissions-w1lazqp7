class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for i in nums:
            if i-1 in nums:
                continue
            j = 0 
            count = 0
            while i+j in nums:
                count += 1
                j += 1
            longest = max(longest, count)
        return longest
