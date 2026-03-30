class Solution:
    def findMin(self, nums: List[int]) -> int:
        cur_mid = 99999
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]
        
        while l <= r:
            mid = (l+r)//2
            m = nums[mid]

            # if sorted array on right half check on left half
            if m < nums[r]:
                if cur_mid > m:
                    cur_mid = m
                r = mid - 1
            else:
                if cur_mid > nums[l]:
                    cur_mid = nums[l]
                l = mid + 1
        return cur_mid
        