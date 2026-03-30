class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # s1 = 0 
        # s2  = 0
        # for i in nums:
        #     s1 += i
        # for j in range(len(nums)+1):
        #     s2 += j
        # return (s2 - s1)

        #converting above code in one loop
        summ = len(nums)

        for i in range(len(nums)):
            summ += i - nums[i]
        return summ