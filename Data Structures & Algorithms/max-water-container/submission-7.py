class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0 , len(height) -1
        leftmax, rightmax = height[l], height[r]
        m = -99999
        while l < r:
            water = min(leftmax, rightmax) * (r-l)
            m = max(water, m)
            if leftmax < rightmax:
                l += 1
                leftmax= max(leftmax, height[l])
            else:
                r -= 1
                rightmax= max(rightmax, height[r])

        return m
