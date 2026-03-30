class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = height[0]
        right_max = height[-1]

        l = 0
        r = len(height) - 1
        water = 0

        while l <= r:
            if left_max < right_max:
                left_max = max(left_max, height[l])
                water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                water += right_max - height[r]
                r -= 1
            print(water)
        return water
            