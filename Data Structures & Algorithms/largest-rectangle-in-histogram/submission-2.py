class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # which stores pair : index, height
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                # we need to pop as we can't extend teh arae further from here
                index, height = stack.pop()
                # compute maxarea
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        # still in stack we can have rectangles
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea