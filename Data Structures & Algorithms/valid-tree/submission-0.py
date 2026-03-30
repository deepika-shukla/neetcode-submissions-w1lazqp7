class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # we have to check if the given graph is the valid tree
        # there should be no loop, plus it should be connected graph
        # for loop we will check if we are visiting again the same node
        # for connected the number of nodes should be eual to visited nodes

        if n < 1:
            return False

        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)

            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n

        
