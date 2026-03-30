class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #here we can use greedy approach starting from last
        #we know we can recah last from last, now we will check for next if we can reach the target
        #if yes that index will become target and then check for next index if we can reach the target
        target = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= target:
                target = i
        return target == 0