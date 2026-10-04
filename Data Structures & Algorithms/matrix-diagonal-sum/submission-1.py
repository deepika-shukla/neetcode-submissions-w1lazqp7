class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        n = len(mat)
        for i in range(n):
            s += mat[i][i]
            s += mat[i][n-i-1]
        
        # we need to remove the mid value sum
        # but only when it exists
        return s - (mat[n//2][n//2] if n &1 else 0)
            
