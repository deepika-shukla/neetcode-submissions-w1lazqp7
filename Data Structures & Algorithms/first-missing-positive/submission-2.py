class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # max_n = abs(max(nums))

        # for i in range(1, max_n + 2):
        #     if i not in nums: # this will cause O(n) complexity
        #         return i
        # # overall around O(N2) complexity

        # first we will mark all negative value as 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # then mark the positions of number as negative
        # negative will tell this number exists
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -1 * (len(nums) + 1)
                
        # whereever you find positive , that index+1 num does not exist
        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i
        
        return len(nums) + 1