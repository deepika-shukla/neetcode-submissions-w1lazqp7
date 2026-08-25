class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        ans = []

        # till both pointers doesn't meet 
        while left < right and top < bottom:
            # we will start with first row
            for i in range(left, right):
                ans.append(matrix[top][i])
            # move the top pointer down
            top += 1

            # now we need last column
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            # we will move right
            right -= 1

            # now here check one edge case in case one row matrix, or one column matrix
            if not ( top < bottom and left < right):
                break # we have got all the values
            
            # In case of complete matrix above condition won't be true therefore now we need last row
            for i in range(right -1, left -1, -1):
                ans.append(matrix[bottom -1][i])
            # update bottom
            bottom -= 1

            # now we need first row
            for i in range(bottom -1, top-1, -1):
                ans.append(matrix[i][left])
            # update left
            left += 1

            # now with updated values sub matrix will carry on
        return ans