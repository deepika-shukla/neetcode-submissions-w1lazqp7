class MedianFinder:

    def __init__(self):
        # We will have two heaps small and large
        # one will be maxheap and one will be minheap
        self.small, self.large = [], []


    def addNum(self, num: int) -> None:
        # First we will add in minheap
        heapq.heappush(self.small, -1*num)

        # now check if the num added is small than numbers in learge heap
        if self.large and (-1 * self.small[0]) > self.large[0]:
            # if not we need to shift in large
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)

        # now balance out the heaps
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((-1 * self.small[0]) + self.large[0])/2
        
        