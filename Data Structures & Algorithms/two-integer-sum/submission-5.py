class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_if_diff = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict_if_diff:
                return [ dict_if_diff[diff], i]
            dict_if_diff[nums[i]] = i
         