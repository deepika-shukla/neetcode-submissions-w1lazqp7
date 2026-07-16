class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra's algorithm
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        print(adj)
        heap = [(0,k)]
        visit = set()
        dist = 0

        while heap:
            t1, s1 = heapq.heappop(heap)
            if s1 in visit:
                continue
            visit.add(s1)
            dist = t1

            # go to neigh 
            for d, t in adj[s1]:
                if d not in visit:
                    heapq.heappush(heap, (t1+t, d))
        return dist if len(visit) == n else -1