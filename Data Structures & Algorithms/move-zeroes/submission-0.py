class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                z = nums.pop(i)
                zeros.append(z)
                continue
            i += 1
        nums += zeros
