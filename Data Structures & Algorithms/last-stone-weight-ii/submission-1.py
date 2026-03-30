class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Now we have to caluculate the minimum weight
        # for this we can choose any two weight
        # we wll use 0/1 knasack algorithm

        # our goal will be ti divde into two sections
        # say 24 is total : 12 and 12 
        # or say 23 is total : 12 and 11
        # and the difference will be the minumu weight

        # also cache the repeated task
        stone_sum = sum(stones)
        target = stone_sum // 2
        def dfs(i, total):
            if total >= target or i == len(stones):
                # this is edge case return diff
                return abs(total - (stone_sum - total))
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(dfs(i+1, total), dfs(i+1, total+stones[i]))

            return dp[(i, total)]

        dp = {}
        return dfs(0, 0)

