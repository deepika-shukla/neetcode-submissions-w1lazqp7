class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)):
            sum = nums[i]
            for j in range(i+1,len(nums)):
                sum += nums[j]
                if sum % k == 0:
                    return True
        return False
