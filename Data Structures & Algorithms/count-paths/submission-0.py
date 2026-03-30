class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tw = [[1]*m]*n
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                tw[i][j] = tw[i+1][j] + tw[i][j+1]      
        return tw[0][0]