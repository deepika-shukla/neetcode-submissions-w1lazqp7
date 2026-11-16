class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # with O(n) space
        # s = set()
        # for i in nums:
        #     if i in s:
        #         return True
        #     s.add(i)
        # return False


        # with O(1) sorting
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False


