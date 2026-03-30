class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        subsets = []
        curset = []
        def backtrack(i):
            if i >= len(nums):
                subsets.append(curset.copy())
                return
            
            curset.append(nums[i])
            backtrack(i+1)

            curset.pop()
            # chcek if no duplicate
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                #ignore thses values
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return subsets