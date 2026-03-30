class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, cur, total):
            if target == total:
                res.append(cur.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            # include candidates[i]
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])

            # do not include candidates[i] and ignore duplicates
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i + 1
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res
