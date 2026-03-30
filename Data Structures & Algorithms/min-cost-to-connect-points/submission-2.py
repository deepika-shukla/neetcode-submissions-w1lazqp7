class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # We will use Prim's algorithm, to find the minimu spanning tree
        # create the edges
        if len(points) == 1:
            return 0
        adj = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                if (x1,y1) not in adj:
                    adj[(x1,y1)] = []
                if (x2,y2) not in adj:
                    adj[(x2,y2)] = []
                adj[(x1,y1)].append([(x2,y2), distance])
                adj[(x2,y2)].append([(x1,y1), distance])

        # print(adj)
        minheap = []
        mst = 0 # minimum weight of graph
        visit = set()
        x, y = points[0]
        heapq.heappush(minheap, [0, (x,y)])
        while minheap:
            wei, node = heapq.heappop(minheap)
            x1, y1 = node

            if node in visit:
                continue
            visit.add(node)
            mst += wei
            for nei, wei in adj[node]:
                heapq.heappush(minheap, [wei, nei])
        return mst

