class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # if total sum is not divisible by k, we cannot divide
        if sum(nums) % k :
            return False

        # get the target sum of each subset
        target = sum(nums) / k

        # reverse the nums which help in failing faster
        nums.sort(reverse=True)

        # keep track of which number is used
        used = [False] * len(nums)

        def backtrack(i, k, subsetsum):
            if k == 0:
                return True # we founf all subsets
            if subsetsum == target:
                return backtrack(0,k-1,0) # we found one subset
            
            for j in range(i, len(nums)):
                if used[j] or subsetsum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j+1,k,subsetsum+nums[j]):
                    return True
                used[j] = False
            return False
        return backtrack(0,k,0)
