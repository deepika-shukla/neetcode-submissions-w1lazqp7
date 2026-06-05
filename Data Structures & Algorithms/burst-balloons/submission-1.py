class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # we need to check if we pop this ballon last

        # for boundaries
        nums = [1] + nums + [1]

        # cache
        cache = {}
    
        def dfs(l,r): # we don;t move l,r they stay at boundary for last ballon computation
            # edge case if l pass r
            # means we tracked all balloon
            if l > r:
                return 0
            
            if (l,r) in cache:
                return cache[(l,r)]
            
            cache[(l,r)] = 0
            for i in range(l, r+1): # traverse through that range
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r) #left and right subproblem
                cache[(l,r)] = max(cache[(l,r)], coins)
            
            return cache[(l,r)]
        
        return dfs(1, len(nums)-2)
