class Solution:
    def trap(self, height: List[int]) -> int:
        # we hav eto find the water trapped between bars
        # we can keep track of the water which could be trapped in each bar

        # left and right max
        l = 0
        r = len(height) - 1
        leftmax, rightmax = height[l], height[r]
        water = 0

        while l < r:
            if leftmax < rightmax:
                # we will ignore first and last since water cannot be trapped there
                l += 1
                leftmax = max(leftmax, height[l])
                water += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                water += rightmax - height[r]
        return water

        

        