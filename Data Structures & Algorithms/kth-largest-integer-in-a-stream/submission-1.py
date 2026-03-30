class KthLargest:
    """To find the kth largest number"""
    def __init__(self, k: int, nums: List[int]):
        # We can have minheao of size k
        self.minHeap, self.k = nums, k
        #rightnow heap is a array we will make it heap
        heapq.heapify(self.minHeap)

        #Now we have to pop the extra elements only have to keep
        #Heap of size k
        # It will pop smallest element only larger element would be there
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        #Now pop the lemeents if the size is larger
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        #we need to return smallest value among three
        return self.minHeap[0]
        
