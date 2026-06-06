class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque() # pairs of [-cnt, ideletime]
        count = Counter(tasks)
        maxheap = [-i for i in count.values()]
        heapq.heapify(maxheap)


        time = 0

        while q or maxheap:
            time += 1
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap) # get the largest repeated character, +1 to reduce cnt since maxheap contains negative numbers
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
        
        return time
