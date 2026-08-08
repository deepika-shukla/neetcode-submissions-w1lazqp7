class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n):
            # we will store its parent
            p = par[n]
            #now check its parent and parent of parent is same or not

            while p != par[p]:
                # if not find the root parent
                par[p] = par[par[p]]
                p = par[p] # move to next generation to check same
            
            #if same, then this is the parent
            return p
        
        def union(n1, n2):
            # find the parents
            p1, p2 = find(n1), find(n2)

            #if both node have same parent, means loop detected
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        # now check for each pair
        for px, py in edges:
            if not union(px,py):
                return [px,py] 