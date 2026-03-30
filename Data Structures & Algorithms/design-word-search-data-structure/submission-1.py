class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root= Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.word = True
        

    def search(self, word: str) -> bool:
        # now here comes the tricky part, since if character is . we need to
        # check for all children

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    # we need to check for children
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            #we found one word
                            return True
                    return False # we didn't find
                else:
                    # the normal logic
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)
        

        
