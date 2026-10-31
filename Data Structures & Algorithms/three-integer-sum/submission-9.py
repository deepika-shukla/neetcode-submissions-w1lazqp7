class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i-1 >=0 and nums[i] == nums[i-1]:
                continue # ignore duplicates

            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l +=1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return ans

