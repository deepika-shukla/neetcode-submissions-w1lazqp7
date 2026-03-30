class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we have to find the maximum water, for that we have to keep track
        #of highes from left and right

        l = 0
        r = len(heights) - 1
        water = 0
        cur = 0

        while l < r:
            l_max= heights[l]
            r_max= heights[r]
            if l_max <= r_max:
                cur = l_max * (r - l)
                l += 1
            else:
                cur = r_max * (r-l)
                r -= 1
            if water < cur:
                water = cur
        return water


 