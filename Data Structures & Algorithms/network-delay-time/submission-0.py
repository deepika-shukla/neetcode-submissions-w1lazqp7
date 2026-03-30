class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # we need to find the max of all the shortest distance
        # from source to all nodes, as that will be the minimum time
        # to reach all nodes
        # we can use dijkstra's algorithm

        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        
        for s,d,w in times:
            adj[s].append([d,w])
        
        minheap = [[0, k]]
        shortest = {} # to keep track of all shortest path
        while minheap:
            # pop the smallest distance
            w1, n1 = heapq.heappop(minheap)

            # if node already in shortest no need to calculate
            if n1 in shortest:
                continue
            
            # if not add in shortets, here we are being greedy since we know
            # all nodes are positive, the valuse will increase not decrease
            shortest[n1] = w1

            # now append in neighbour in heap to find shortest among them
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, [w1+w2, n2])
        
        # if for all nodes we are able to calculate return max of it
        if len(shortest) == n:
            return max(shortest.values())
        else:
            return -1