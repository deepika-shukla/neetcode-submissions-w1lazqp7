class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[0,-1], [-1,0], [1,0], [0,1]]
        visit = set()

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O" or (r,c) in visit:
                return
            board[r][c] = "Y"
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        # call edge O
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O") and (r in [0, rows-1] or c in [0, cols-1]):
                    dfs(r,c)
        
        # make other O as X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # now make Y as O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Y":
                    board[r][c] = "O"
