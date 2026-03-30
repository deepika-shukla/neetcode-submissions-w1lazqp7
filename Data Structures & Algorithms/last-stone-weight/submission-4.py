class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we need max heap, we can pop highest weight stone first
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            
            if a == b:
                continue
            else:
                heapq.heappush(stones, a-b)
        return -stones[0] if stones else 0
