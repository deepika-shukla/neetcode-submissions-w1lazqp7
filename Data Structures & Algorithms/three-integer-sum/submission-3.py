class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #we will sort the list
        nums.sort()
        res = []

        #starting from each number we will calculation the summ
        for i in range(len(nums)):
            #ignore the duplicate calculations
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                threesum = nums[l] + nums[r] + nums[i]

                #if greater than 0
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    #we found 1 solution
                    res.append([nums[l],nums[r],nums[i]])
                    l += 1
                    r -= 1

                    #now ignore duplicate calculations
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

