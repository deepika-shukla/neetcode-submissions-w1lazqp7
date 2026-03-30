class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # first we need to find the peak
        length = mountainArr.length() # we know the peak wont we on 0th or last index
        l, r = 1, length - 2
        
        while l <= r:
            m = (l+r) // 2
            # get three values
            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)

            if left < mid < right:
                # our peak will be on right
                l = m + 1
            elif left > mid > right:
                # our peak on left
                r = m -1
            else:
                # we found the peak
                break
        peak = m

        # search in left
        l, r = 0, peak - 1

        while l <= r:
            m = (l+r) // 2
            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) > target:
                r = m - 1
            else:
                l = m + 1

        # search in right
        l, r = peak, length - 1

        while l <= r:
            m = (l+r) // 2
            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) > target:
                l = m + 1
            else:
                r = m - 1
        return -1