class Solution:
    def findMin(self, nums: List[int]) -> int:
        # one sorted array either in left or right

        l, r = 0 , len(nums) - 1
        small = 9999999
        while l <= r:
            mid = (l+r) //2
            if mid -1 >= 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[l] <= nums[mid]:
                small = min(small,nums[l])
                l = mid + 1
            else:
                small = min(small,nums[mid])
                r = mid - 1
        return small

             