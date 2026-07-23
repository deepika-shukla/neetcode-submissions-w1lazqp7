class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # we need to find the cheapest flight at most k stops
        # so, for that times we will calculate min distance
        # if we are not able to reach destination, then return -1

        # create array for each airport, the distance is infinite
        prices = [float("inf")] * n
        # source will be 0
        prices[src] = 0

        for i in range(k+1):
            temp = prices.copy()
            for s,d,p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p
            prices = temp
        
        return -1 if prices[dst] == float("inf") else prices[dst]
            