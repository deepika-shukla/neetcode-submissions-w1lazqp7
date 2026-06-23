class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(2, n+1):
            temp = two
            two = one + two # total step to reach current position is sum of previous steps
            one = temp
        return two
