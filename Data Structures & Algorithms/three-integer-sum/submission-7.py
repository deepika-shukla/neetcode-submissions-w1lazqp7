class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue
            n1 = nums[i]

            # now we will find n1's pair
            l, r = i+1, len(nums) - 1
            while l < r:
                s = n1 + nums[l] + nums[r]
                if s  == 0:
                    res.append([nums[l],nums[i],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return res