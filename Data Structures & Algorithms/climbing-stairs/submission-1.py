class Solution:
    def climbStairs(self, n: int) -> int:
        # #recursion
        # #we know we have two choices one or two step
        # if n == 0:
        #     #we reached the destination
        #     return 1
        # if n < 0:
        #     #we didn't reach
        #     return 0
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # DP
        # we know our resulte depend on two values
        # we start from left and keep calculating till start
        # we will get all the distinct ways
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
        return one
        
