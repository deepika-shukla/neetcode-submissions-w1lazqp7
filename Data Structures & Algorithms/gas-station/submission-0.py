class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # we have to calculate the starting point in such a way
        # we complete a circle

        # first thing to consider is if we have less gas as compared to cost
        # we can never reach
        if sum(gas) < sum(cost):
            return -1
        
        # if we have enough gas find the start by checking each point
        start = 0
        total = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            # check if total gets less than 0
            if total < 0:
                #make total initialise to 0, and start to next index
                total = 0
                start = i+1
        return start