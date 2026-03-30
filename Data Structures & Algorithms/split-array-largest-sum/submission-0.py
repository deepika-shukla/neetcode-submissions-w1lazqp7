class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # we will use binary serach
        # the max sum can be total sum in array
        # and min sum can be max in nums

        # we also need to check for each sum, are we able to spilt subarray
        def canSplit(largest):
            subarray = 1
            cursum = 0

            for n in nums:
                cursum += n
                if cursum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    cursum = n # because we will use in subarray
                
            return True

        l,r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l+r)//2

            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res