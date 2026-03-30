class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-1 * i for i in gifts]
        heapq.heapify((gifts))

        for i in range(k):
            get = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int((get)**(1/2)))
        
        ans = 0
        for i in gifts:
            ans += (-1)*i
        
        return ans

