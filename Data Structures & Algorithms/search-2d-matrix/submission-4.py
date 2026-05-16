class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])
        row = 0
        while row < rows:
            if not (matrix[row][0] <= target <= matrix[row][-1]):
                row += 1
                continue

            l,r = 0, cols -1

            while l <= r:
                mid = (l+r)//2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            row += 1
        return False