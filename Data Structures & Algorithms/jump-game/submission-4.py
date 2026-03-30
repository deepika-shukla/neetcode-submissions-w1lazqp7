class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we will start from last index and check 
        # if we are able to reach last index then update the index
        # until reach the start

        last_index = len(nums) - 1

        for i in range(last_index-1, -1,-1):
            if nums[i] + i >= last_index:
                last_index = i
        
        if last_index == 0:
            return True
        return False