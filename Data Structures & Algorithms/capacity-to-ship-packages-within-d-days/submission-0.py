class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # we can have either the max of weight as min capacity
        # or sum of all weights
        l, r = max(weights), sum(weights)
    
        def isCap(cap):
            ships, curcap = 1, cap

            for w in weights:
                if curcap - w < 0:
                    # we reached limit, now we need new ship
                    ships += 1
                    curcap = cap
                curcap -= w
            return ships <= days
                

        res = r
        while l <= r:
            m = (l+r)//2

            if isCap(m):
                res = min(res, m)
                # then try to find minimum
                r = m-1
            else:
                l = m +1
        return res