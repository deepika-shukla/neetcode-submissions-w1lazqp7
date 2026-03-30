class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0

        # we can use two pointer method and look for high value
        l = 0
        r = len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                water = max(water, (r - l) * heights[l])
                l += 1
            else:
                water = max(water, (r - l) * heights[r])
                r -= 1
        return water