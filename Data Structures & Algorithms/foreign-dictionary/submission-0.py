class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()
        
        for i in range(len(words) - 1):
            # we will start with first two
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                # this is wrong as per question, we will directly return ""
                return ""
            # Now we will fill our adjacency list
            # with how many letters comes after
            for j in range(minlen):
                if w1[j] != w2[j]:
                    # we found mismatch character add in adj 
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} # True -  current path, False - visit
        res = []
        def dfs(char):
            if char in visit:
                return visit[char]
            visit[char] = True
            for nei in adj[char]:
                if dfs(nei): # if we are getting true, it means cycle
                    return ""
            visit[char] = False
            # now we can add the char in result
            res.append(char)
        
        for char in adj:
            if dfs(char):
                return ""
            
        res.reverse()
        return "".join(res)