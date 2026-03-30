class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we have three conditions:
        # 1. when we found the answer
        # 2. when index reaches out of index
        # 3. when curSUM > target

        # we will calculate sum using help function
        # and store result in our res list
        res = []

        # we need to keep track of three things: index, curlist, cursum
        def helper(i, cur, cursum):
            # now if index is greater or target is greater we don't
            # want to store any thing
            if i >= len(nums) or cursum > target:
                return

            # check if we found the target
            if cursum == target:
                res.append(cur.copy())
                return # as we don't want to calculate further for this subset
            # now include the current number
            cur.append(nums[i])
            helper(i,cur, cursum+nums[i])
            # now backtrack if we didn't find the solution in DFS
            # first pop that number
            cur.pop()
            #now we will check from next index and not include previous
            #number in the sum
            helper(i+1,cur, cursum)
        
        helper(0,[],0)
        return res

