class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if r not in range(len(board)) or c not in range(len(board[0])) or board[r][c] != word[i] or (r,c) in visit:
                return False
            
            visit.add((r,c))
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1)
                  or dfs(r,c+1,i+1) or  dfs(r,c-1,i+1))
            visit.remove((r,c))

            return res
        
        # now check for rach point
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
                
        return False