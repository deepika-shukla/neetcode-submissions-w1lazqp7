# class NumMatrix:

#     def __init__(self, matrix: List[List[int]]):
#         # what we will do it store the total sum at each point 
#         # which form the rectangle.
#         # for example our grid is 4X4, for each for point
#         # we will store the sum from start, which will help to
#         # calculate the sum for the range
#         # now for our edge case we can go out of bound
#         # therefore we will take one extra row and col
#         rows, cols = len(matrix), len(matrix[0])
#         self.sumMatrix = [[0] * (cols+1) for _ in range(rows + 1)]

#         for r in range(rows):
#             # we will have our prefix
#             prefix = 0
#             for c in range(cols):
#                 # +1 because first row, col will be zero
#                 prefix += matrix[r][c] # the current value in matrix
#                 above = self.sumMatrix[r][c+1] # the sum above it
#                 self.sumMatrix[r+1][c+1] = prefix + above
#         print(self.sumMatrix)



#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         # now we will calculate sum of the given rectangle only using prefix sum
#         # and since we are subtracting the above row and left coloumn, the first number(topleft)
#         # will be substracted twice, to prevent that we will readd

#         # also our self.sumMatrix has 1 extra row, col
#         r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1

#         # calculate the positions
#         bottomRight = self.sumMatrix[r2][c2]
#         above = self.sumMatrix[r1-1][c2] # prefix
#         left = self.sumMatrix[r2][c1-1]
#         topLeft = self.sumMatrix[r1-1][c1-1] # the element which we will substarct twice

#         return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.prefix = [[0 for i in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

        # we need to calculate the prefix sum
        # the prefix sum = left + above
        for r in range(len(matrix)):
            prefix = 0
            for c in range(len(matrix[0])):
                prefix += self.matrix[r][c]
                above = self.prefix[r][c+1]
                self.prefix[r+1][c+1] = prefix + above
                
                
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # now to calculate we will make use of prefix sum
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        bottomright = self.prefix[r2][c2]
        topleft = self.prefix[r1-1][c1 -1]
        left = self.prefix[r2][c1-1]
        above = self.prefix[r1-1][c2]

        return  abs(bottomright + topleft - above - left)
