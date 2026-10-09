class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, curSum):
            if curSum == target:
                res.append(cur.copy())
                return
            
            if curSum > target:
                return
            
            if i == len(nums):
                return

            curSum += nums[i]
            cur.append(nums[i])
            backtrack(i, cur, curSum)
            curSum -= nums[i]
            cur.pop()
            backtrack(i+1, cur, curSum)
        
        backtrack(0, [], 0)
        return res