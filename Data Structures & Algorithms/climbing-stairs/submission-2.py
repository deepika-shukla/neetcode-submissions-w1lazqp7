class Solution:
    def climbStairs(self, n: int) -> int:
        
        def find(i, count):
            if i > n:
                return 0
            if i == n:
                count += 1
                return count
            return find(i+1, count) + find(i+2, count)
        return find(0, 0)
