class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        cols = set()
        posdiag = set()
        negdiag = set()

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c in cols or r+c in posdiag or r-c in negdiag:
                    continue
                
                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                backtrack(r+1)
                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
            
        
        backtrack(0)
        return res