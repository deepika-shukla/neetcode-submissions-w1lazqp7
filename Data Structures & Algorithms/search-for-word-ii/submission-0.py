class Trie:
    def __init__(self):
        self.children = {}
        self.last = False
    
    def addWord(self, word):
        cur = self

        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.last = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for wo in words:
            root.addWord(wo)
        rows, cols = len(board), len(board[0]) 
        res, visit = set(), set()
        def dfs(r, c, node, word):
            if r not in range(len(board)) or c not in range(cols) or (r,c) in visit or board[r][c] not in node.children:
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c] 
            if node.last:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,'')
        
        return list(res)