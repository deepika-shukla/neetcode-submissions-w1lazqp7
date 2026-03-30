class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #we have to find all the combinations adding to the sum
        #and for unique we can sort so will eliminate to check for smae number twice
        candidates.sort()
        res = [] #to store final answer

        #we will do backtracking either to include the next number ot not
        def backtrack(i, cur, summ):
            #edge cases
            if summ == target:
                res.append(cur.copy())
                return
            if i == len(candidates) or summ > target:
                return
            
            cur.append(candidates[i])
            backtrack(i+1, cur, summ + candidates[i])
            #pop the last element
            cur.pop()

            #check if repeated element
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, cur, summ)
        backtrack(0,[],0)
        return res


