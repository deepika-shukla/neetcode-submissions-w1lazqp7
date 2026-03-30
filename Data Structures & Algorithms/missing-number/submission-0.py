class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s1 = 0 
        s2  = 0
        for i in nums:
            s1 += i
        for j in range(len(nums)+1):
            s2 += j
        return (s2 - s1)