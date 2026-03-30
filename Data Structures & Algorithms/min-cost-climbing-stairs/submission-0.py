class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # to find the minimum cost we have two choices 1 or 2 jump
        #we start from last as we need to know the minimum cost required to reach from last
        #then we can calculate for a place earlier to it

        #since we have two option so our answer depend on either just next to that
        #point or next to it
        #so we add a 0 to our list to make it easy
        cost.append(0)

        #now we will start from third last, whose output would epend on second last and last
        for i in range(len(cost)-3,-1,-1):
            #calculate the minimum cost
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
        
        #then return the minimum from 0 and 1st position as we had two option
        return min(cost[0], cost[1])
        