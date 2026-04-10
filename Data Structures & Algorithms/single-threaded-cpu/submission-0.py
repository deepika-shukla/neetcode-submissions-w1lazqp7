class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # first include index in tasks
        for i, t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key = lambda t : t[0])

        res, minheap =[], []
        i, time = 0, tasks[0][0]

        while minheap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minheap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not minheap:
                # cpu is idle, forward the time
                time = tasks[i][0]
            
            else:
                # get the index of least processing time
                proctime, index = heapq.heappop(minheap)
                time += proctime
                res.append(index)
        return res