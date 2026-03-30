class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #first we include 1 at each side
        nums = [1] + nums + [1]
        #cache the result in dp
        dp = {}

        #recursive fucntion to check for each element
        def dfs(l,r):
            #if out of bounce
            if l > r:
                return 0 #number of coins
            
            if (l,r) in dp: 
                return dp[(l,r)]
            
            #if does not exist
            dp[(l,r)] = 0

            #check for each element if it is popped at last
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                #now check for its left and right subarray
                coins += dfs(l, i-1) + dfs(i+1,r)
                #update the dp
                dp[(l,r)] = max(dp[(l,r)], coins)
            return dp[(l,r)]
        
        return dfs(1, len(nums)-2)