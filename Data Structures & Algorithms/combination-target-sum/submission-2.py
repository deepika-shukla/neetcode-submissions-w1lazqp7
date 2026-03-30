class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we have two choices either keep including the number
        # or move to next index

        # to store all pairs
        res = []

        def find(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            #if we reached last index
            if i == len(nums) or total > target:
                return
            
            cur.append(nums[i])
            find(i, cur, total+nums[i])
            cur.pop()
            find(i+1, cur, total)
        
        find(0, [], 0)
        return res