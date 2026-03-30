class KthLargest:
    # in this question we we will maintain min heap of size k 
    # as the minimum element won't be in our use since we we want largest number
    # also in question we are getting only add element function
    # therefore we will pop the small number, and we will be left with k elements and
    # 0 index will be kth largest element

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
