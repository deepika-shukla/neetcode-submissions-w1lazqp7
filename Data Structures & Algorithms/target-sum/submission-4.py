class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ########## recursive

        # def helper(i, total):
        #     if i == len(nums):
        #         return total == target
            
        #     # include both scenerio
        #     return helper(i+1, total - nums[i]) + helper(i+1, total + nums[i])
        # return helper(0, 0)
        
        
        ######### memoization
        dp = {}

        def helper(i, total):
            if (i,total) in dp:
                return dp[(i, total)]
            if i == len(nums):
                return total == target
            
            dp[(i,total)] = helper(i+1, total - nums[i]) + helper(i+1, total + nums[i])
            return dp[(i,total)]
        return helper(0,0)

            