class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # one thing to keep in mind, no matter the number
        # of bananas in the pile, koko will take an hour to finish the bananas

        # also we know the max number of bananas could be eaten
        # is the max in the given piles, and starting from 1

        l, r = 1, max(piles)
        res = r # highest bananas

        # now do binary search to find the minimum bananas/hour
        while l <= r:
            # calculate hours
            hours = 0
            k= (l+r)//2

            #for every piles together
            for p in piles:
                #remember for everypile it will be 1 hour
                hours += math.ceil(float(p)/k)
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res