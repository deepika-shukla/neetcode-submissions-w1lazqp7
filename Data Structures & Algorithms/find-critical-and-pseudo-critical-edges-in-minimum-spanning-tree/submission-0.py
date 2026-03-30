class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n) ]
        self.rank = [1] * n
    
    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True        

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        mst = 0
        for i, e in enumerate(edges):
            e.append(i) # appending the original index

        edges.sort(key=lambda e: e[2]) # based on weight

        uf = UnionFind(n)
        for v1, v2, w , i in edges:
            if uf.union(v1,v2):
                mst += w
        
        critical, psuedo = [],[]
        for n1, n2, e_weight, i in edges:
            #Try without curr edge
            weight = 0
            uf = UnionFind(n)
            for v1,v2,w,j in edges:
                if i !=j and uf.union(v1,v2): # weight of one edge won't be included each time
                    weight += w

            # now compare if both weigth and mst weight are equal
            # if not we are not able to acheive mst, this edge was required
            if max(uf.rank) != n or weight > mst:
                critical.append(i) # append the index
                # Now we know critical edge will not be psuedo edge we will continue
                continue

            
            # if we didn;t find critical edge
            # Try with curr edge if it is psuedo
            uf = UnionFind(n)
            uf.union(n1, n2)
            weight = e_weight
            for v1, v2, w, j in edges:
                if uf.union(v1,v2):
                    weight += w
            
            # now if weight is equal to mst weight, it means it is atleast
            # part of some mst 
            if weight == mst:
                psuedo.append(i) # append the index
        return [critical, psuedo]

                

                
            