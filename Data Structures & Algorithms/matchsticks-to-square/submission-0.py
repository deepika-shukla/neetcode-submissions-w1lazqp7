class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # now we need to combine the matchsticks to form 4 sides of square
        # we know all the sides should be equal, and if total sum of
        # matchsticks is not divisible by 4 we can't make a square

        length_of_each_side = sum(matchsticks) // 4
        # we are keeping the track of sides
        side = [0] * 4

        if sum(matchsticks) / 4 != length_of_each_side:
            return False
        
        # now we will reverse the matchsticks
        matchsticks.reverse()
        # we did the reverse in case we have matchstick greater than the length
        # allowed we can check them first and do not spend checking till last

        def backtrack(i):
            # if we are able to reach last, we found one solution
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if side[j] + matchsticks[i] <= length_of_each_side:
                    side[j] += matchsticks[i]
                    # and check for next side
                    if backtrack(i+1):
                        return True # we found one solution
                    side[j] -= matchsticks[i]
            return False
        return backtrack(0)