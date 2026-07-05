class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min, cur_max = 1, 1
        res = max(nums)

        for n in nums:
            # if n == 0, then we can reset produc
            if n == 0:
                cur_min, cur_max = 1, 1
                continue

            temp = n * cur_max
            cur_max = max(n, n*cur_max, n*cur_min)
            cur_min = min(n,n*cur_min, temp)

            res = max(res, cur_max)
        return res