class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []
        res = []
        count = {}
        for n in nums:
            count[n] =  1 + count.get(n, 0)
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()
                    perm.pop()
                    count[n] += 1
                    

        dfs()
        return res