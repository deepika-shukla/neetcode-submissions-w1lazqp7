class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            curr = 0
            if i-1 in nums:
                continue
            while i in nums:
                curr += 1
                i += 1
            if count < curr:
                count = curr
        return count
        