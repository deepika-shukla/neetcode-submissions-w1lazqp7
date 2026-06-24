class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we will have one part as sorted array in the rotated array

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            # now check for left sorted array
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid -  1 # search left
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1
