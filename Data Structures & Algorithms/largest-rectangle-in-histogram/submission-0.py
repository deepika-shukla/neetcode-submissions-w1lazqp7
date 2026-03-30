class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        # we will try to compute the laregets area at that index
        # and store height and index in statck
        #in ccase we get lower height than previous one so it 
        # it needs to be popped since we extend it further
        #but we will store its index and it could extend backward
        #also calculate max area

        stack = [] # pairs: [index, height]

        maxArea = 0 
        for i, h in enumerate(arr):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, (height * (i - index)))
                start = index
            stack.append([start, h])
        
        #now traverse the remaining stack but not from top
        for i, h in stack:
            maxArea = max(maxArea, h * (len(arr) - i))
        return maxArea

