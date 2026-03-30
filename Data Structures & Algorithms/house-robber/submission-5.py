class Solution:
    def rob(self, nums: List[int]) -> int:
        rob0, rob1 = 0, nums[0]

        for i in range(1, len(nums)):
            temp = rob1
            rob1 = max(nums[i]+rob0, rob1)
            rob0 = temp
        
        return max(rob1, rob0)
