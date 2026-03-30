class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # subset = []
        # res = []
        # def helper(i):
        #     if i >= len(nums): # we reached at last
        #         res.append(subset.copy()) # since in res, the list is getting copied and when we modify the subset list it will be modified at all places, therefore we will append the copy of subset
        #         return
        #     subset.append(nums[i])
        #     helper(i+1)
        #     subset.pop() # backtrack
        #     helper(i+1)
        # helper(0)
        # return res



        ########### Iterative ############
        res = [[]]   # start with the empty subset

        for num in nums:
            new_subsets = []           # hold all subsets created in this iteration

            for subset in res:         # iterate over all existing subsets
                new_subset = subset + [num]  # make a copy and add current num
                new_subsets.append(new_subset)

            res += new_subsets          # merge the new subsets into result

        return res

        