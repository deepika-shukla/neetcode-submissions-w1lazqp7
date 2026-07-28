class Solution:
    def specialArray(self, nums: List[int]) -> int:

        # brute force
        ans = -1
        
        for x in range(0, max(nums)+1):
            count = 0
            for i in nums:
                if i >= x:
                    count += 1
            if count == x:
                ans = x
        return ans
