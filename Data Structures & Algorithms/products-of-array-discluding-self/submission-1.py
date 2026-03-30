class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prev =[1]*len(nums)
        post =[1]*len(nums)

        for i in range(1, len(nums)):
            prev[i] = prev[i-1]*nums[i-1]
        print(prev)
        
        for j in range(len(nums)-2,-1,-1):
            post[j] = post[j+1]*nums[j+1]
        print(post)

        for i in range(len(nums)):
            ans.append(prev[i]*post[i])
        return ans

