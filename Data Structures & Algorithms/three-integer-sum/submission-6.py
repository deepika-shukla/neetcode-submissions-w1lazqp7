class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        # -4, -1, -1, 0, 1, 2
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                s =  nums[l] + nums[i] + nums[r]
                if s == 0:
                    ans.append([nums[l],nums[i],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
            
        return ans