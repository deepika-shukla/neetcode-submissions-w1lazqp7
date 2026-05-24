class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # we need to keep track of:
        # max prod :  for postivi numbers
        # min prod  : for negative number, which can create largeer product if in even count

        cur_min, cur_max = 1,1
        res = max(nums)

        for n in nums:
            # if zero, we can ignore, it will give only 0
            if n ==0:
                cur_min, cur_max = 1,1
                continue
            
            temp = n*cur_max
            cur_max = max(n, n*cur_max, n*cur_min)
            cur_min = min(n, temp, n*cur_min)
            
            res = max(res, cur_max)
        return res