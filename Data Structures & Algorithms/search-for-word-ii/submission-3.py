class Trie:
        def __init__(self):
            self.children = {}
            self.end = False
class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.end = True
        
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r,c,node,w):
            # edge cases
            if r<0 or r >= rows or c <0 or c >= cols or board[r][c] not in node.children or (r,c) in visit:
                return 
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            w += board[r][c]
            if node.end:
                res.add(w)

            dfs(r+1,c,node,w)
            dfs(r,c+1,node,w)
            dfs(r-1,c,node,w)
            dfs(r,c-1,node,w)

            visit.remove((r,c))
        
        # traverse whole board
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)

