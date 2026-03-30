class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we have to find the points near to the origin
        #First we will find the distance
        minheap = []
        for p in points:
            x,y = p
            dist = (x**2) + (y**2)
            minheap.append((dist, x, y))
        
        heapq.heapify(minheap)
        res = []
        for i in range(k):
            d,x,y = heapq.heappop(minheap)
            res.append([x,y])
        return res

