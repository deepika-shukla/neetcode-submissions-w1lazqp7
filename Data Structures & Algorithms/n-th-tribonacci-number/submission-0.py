class Solution:
    def tribonacci(self, n: int) -> int:
        one = 0
        two = 1
        three = 1
        if n == 0:
            return 0

        if n <= 2:
            return 1
        
        for i in range(n-3, -1, -1):
            temp1, temp2 = two, three
            three = one + two + three
            two = temp2
            one = temp1
        return three