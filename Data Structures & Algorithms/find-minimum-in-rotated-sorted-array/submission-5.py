class Solution:
    def findMin(self, nums: List[int]) -> int:
        # on rotating teh array we could notice
        # one thing either left or right side of the array is
        # sorted, so we can store the smallest one and 
        #  move on to another part to find if another smallest exist

        l = 0
        r = len(nums) - 1
        small = 999999

        while l <= r:
            mid = (l+r)//2

            if nums[l] <= nums[mid]:
                small = min(small, nums[l])
                # now move to next part iof any smaller number exist
                l = mid +1
            else:
                small = min(small, nums[mid])
                r = mid - 1
        return small



