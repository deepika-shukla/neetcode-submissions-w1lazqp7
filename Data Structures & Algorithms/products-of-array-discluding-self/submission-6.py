class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1] * len(nums)
        # suffix = [1] * len(nums)

        # for i in range(len(nums)):
        #     if i-1 >= 0:
        #         prefix[i] = prefix[i-1] * nums[i-1]

        # for i in range(len(nums)-1,-1,-1):
        #     if i+1 < len(nums):
        #         suffix[i] = suffix[i+1] * nums[i+1]
  
            
        # for i in range(len(nums)):
        #     prefix[i] *= suffix[i]

        # return prefix

        ans = [1] * len(nums)

        for i in range(1, len(nums)):
            ans[i] = nums[i-1] * ans[i-1]
        
        postfix = 1
        for i in range(len(nums) -1, -1,-1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans






