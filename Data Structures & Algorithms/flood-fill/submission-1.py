class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orginal = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        directions = [[0,1],[-1,0], [1,0], [0,-1]]
        visit = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or image[r][c] != orginal or (r,c) in visit:
                return

            image[r][c] = color
            visit.add((r,c))
            for dr, dc in directions:
                row, col = dr+r, dc+c
                dfs(row, col)
        
        dfs(sr, sc)
        return image
