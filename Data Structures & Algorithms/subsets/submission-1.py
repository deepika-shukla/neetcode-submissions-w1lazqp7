class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        def helper(i):
            if i >= len(nums): # we reached at last
                res.append(subset.copy()) # since in res, the list is getting copied and when we modify the subset list it will be modified at all places, therefore we will append the copy of subset
                return
            subset.append(nums[i])
            helper(i+1)
            subset.pop() # backtrack
            helper(i+1)
        helper(0)
        return res