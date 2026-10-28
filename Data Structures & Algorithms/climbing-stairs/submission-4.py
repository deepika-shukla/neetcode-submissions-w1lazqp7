class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            temp = two
            two = one + two
            one = temp
        return two


        # recusrive approach
        # def find(start):
        #     if start == n:
        #         return 1
        #     if start > n:
        #         return 0
            
        #     return find(start+1) + find(start+2)
        # return find(0)