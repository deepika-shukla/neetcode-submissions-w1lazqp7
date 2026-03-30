class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            print(i)
            l = 0
            r = len(i) - 1
            if i[0] <= target <= i[r]:
                while l <= r:
                    m = (l + r)//2

                    if i[m] == target:
                        return True
                    elif i[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
            else:
                continue
        return False
