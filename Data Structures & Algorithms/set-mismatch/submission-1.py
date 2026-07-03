class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 1]
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                res[0] = nums[i]
            elif nums[i] - nums[i - 1] == 2:
                res[1] = nums[i] - 1

        if nums[-1] != len(nums):
            res[1] = len(nums)
        return res