class Solution:
    def maxArea(self, h: List[int]) -> int:
        
        l = 0
        r = len(h)-1
        area = 0
        while l <= r:
            leftmax, rightmax = h[l], h[r]
            if leftmax > rightmax:
                cur = (r-l) * min(leftmax, rightmax)
                area = max(area, cur)
                r -= 1
            else:
                cur = (r-l) * min(leftmax, rightmax)
                area = max(area, cur)
                l += 1
        return area
