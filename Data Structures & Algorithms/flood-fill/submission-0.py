class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visit = set()
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        if image[sr][sc] == color:
            return image
        def dfs(r,c, col):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != col or (r,c) in visit:
                return
            image[r][c] = color

            visit.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, col)
        
        dfs(sr,sc,image[sr][sc] )
        return image
