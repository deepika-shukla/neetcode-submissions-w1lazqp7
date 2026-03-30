class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj = {}
        # add keys to the adj dictionary
        for i in range(n):
            adj[i] = []
        
        for s, d, w in edges:
            adj[s].append([d,w])
        
        # create a min heap with start node, to keep track
        # of all smaller distances
        minheap = [[0, src]] # (weight, node)

        # we will keep track of the shortest
        shortest = {}
        while minheap:
            # pop the smallest one
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            
            shortest[n1] = w1
            
            # search its neighbour and add in heap
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, [w1+w2, n2])
        
        # Fill the missing nodes
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest


