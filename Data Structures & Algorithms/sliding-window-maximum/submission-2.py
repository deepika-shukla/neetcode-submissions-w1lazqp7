class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        l1 = []
        while r < len(nums):
            while len(nums[l:r]) != k:
                r += 1
                
            
            l1.append(max(nums[l:r]))
            l += 1
        return l1