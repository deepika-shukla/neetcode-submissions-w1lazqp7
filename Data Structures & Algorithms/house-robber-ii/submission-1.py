class Solution:
    def rob(self, nums: List[int]) -> int:
        return max( nums[0], self.helper(nums[1:]), self.helper(nums[0: -1]))
        
    
    def helper(self, nums):
        rob0, rob1 = 0, 0

        for i in range(len(nums)):
            temp = rob1
            rob1 = max(rob0+nums[i], rob1)
            rob0 = temp
        return max(rob0, rob1)