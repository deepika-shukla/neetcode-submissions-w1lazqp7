# class Solution:
#     def mySqrt(self, x: int) -> int:
#         min_diff = 9999
#         ans = 0
#         for i in range(1, x+1):
#             if x // i == i:
#                 return i
#             else:
#                 sq = i*i #
#                 val = x - sq 
#                 if 0 < val and val < min_diff:
#                     min_diff = val
#                     ans = i
#         return ans

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        res = 1
        for i in range(1, x + 1):
            if i * i > x:
                return res
            res = i

        return res