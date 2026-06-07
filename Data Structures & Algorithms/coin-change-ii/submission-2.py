class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # #recursive

        # def backtrack(i, total):
        #     if i == len(coins):
        #         return 0
        #     if total == amount:
        #         return 1
            
        #     c = 0
        #     if total < amount:
        #         c = backtrack(i+1, total)
        #         c += backtrack(i, total+coins[i])
        #     return c
        
        # return backtrack(0,0)

        ### memoization
        cache = {}

        def backtrack(i, total):
            if i == len(coins):
                return 0
            if (i, total) in cache:
                return cache[i,total]
            
            if total == amount:
                return 1
            
            c = 0
            if total < amount:
                c = backtrack(i+1, total)
                c += backtrack(i, total+coins[i])
            cache[(i,total)] = c

            return cache[(i,total)]
        
        return backtrack(0,0)