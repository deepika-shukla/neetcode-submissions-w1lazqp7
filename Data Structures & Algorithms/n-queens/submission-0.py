class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # we can put either queen on alternate col,
        # alternate positive diagonal, or negative diagonal
        # as queen can move left/right/up/down and diagonal

        res = []
        cols = set()
        posdiag = set()
        negdiag = set()
        board = [["."]*n for i in range(n)]

        def backtrack(r):
            if r == n:
                # we found the solution
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r-c) in negdiag or (r+c) in posdiag:
                    continue
                
                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res
