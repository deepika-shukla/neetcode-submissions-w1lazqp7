class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        curr= nums[0]
        for i in nums:
            if summ < 0:
                summ = 0
            
            summ += i
            curr = max(curr,summ)
        return curr
            
        