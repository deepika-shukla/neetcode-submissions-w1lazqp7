class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=99999999
        cursum = 0
        l = 0
        change = False
        for r in range(len(nums)):
            cursum += nums[r]

            while cursum >= target:
                min_len = min(min_len, r-l+1)
                cursum -= nums[l]
                change = True
                l += 1
            
        return min_len if change else 0
                
