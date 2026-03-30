class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            cur = 0
            if i-1 not in nums:
                j = 0
                while (i+j) in nums:
                    cur += 1
                    j+=1
                    if cur > count:
                        count = cur
        return count

