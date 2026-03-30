class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we need to find the product of each index but
        # the number on that index.

        #we can find prev and post product and to get the final result
        # multiply them

        prev = 1
        post = 1

        arr = [1] * (len(nums)) # [1,1,2,8,1]
        # [48,24,6,1,1]
        for i in range(1, len(nums)):
            arr[i] = nums[i-1] * arr[i-1]
        print(arr)
        new = [1] * (len(nums))
        for i in range(len(nums)-2, -1, -1): #0
            new[i] = nums[i+1] * new[i+1]
        
        t = [1]*len(nums)
        for i in range(len(nums)):
            t[i] = arr[i]*new[i]
        
        return t
