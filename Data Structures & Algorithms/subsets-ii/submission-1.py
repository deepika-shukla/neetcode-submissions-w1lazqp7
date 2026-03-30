class Solution:
    def subsetsWithDup(self, l: List[int]) -> List[List[int]]:
        res = []
        # sort the list
        l.sort()

        #then fuction to get all subsets
        def backtrack(i, nums): # index and current list
            if i == len(l):
                #we reached last of list
                res.append(nums.copy())
                return
            
            # now we two option either to include or not include
            # include l[i]
            nums.append(l[i])
            backtrack(i+1, nums)

            nums.pop()
            # also check for duplicates
            while i+1 < len(l) and l[i] == l[i+1]:
                i += 1
            
            backtrack(i+1, nums)
        backtrack(0, [])
        return res