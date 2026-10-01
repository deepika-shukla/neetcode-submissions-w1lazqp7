class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(matrix) for i in range(len(matrix[0]))]
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                ans[j][i] = matrix[i][j]
        return ans

