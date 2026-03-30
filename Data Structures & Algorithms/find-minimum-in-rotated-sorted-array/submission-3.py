class Solution:
    def findMin(self, nums: List[int]) -> int:

        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         return nums[i]
        # return nums[0]

        # using binary search
        l = 0
        r = len(nums) -1 

        min_number = 10000
        while l < r:
            m = (l + r)//2
            if min_number > nums[m]:
                min_number = nums[m]

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        # in case l and r becomes equal
        if min_number > nums[l]:
            min_number = nums[l]
        return min_number

