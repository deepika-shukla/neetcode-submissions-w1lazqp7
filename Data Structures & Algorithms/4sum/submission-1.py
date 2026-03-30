class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        # first fixed pointer
        for i in range(n):
            l = []
            # ignore duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # next fixed pointer will be j
            for j in range(i+1, n):
                #ignore duplicate
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # now get your left and right pointer
                left = j+1
                right = n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        l = [nums[i], nums[j], nums[left], nums[right]]
                        ans.append(l)
                        left += 1
                        right -= 1
                        # ignore duplicate at this case as well
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
                        while left < right and nums[right] == nums[right-1]:
                            right -=1
                    elif target > current_sum:
                        left += 1
                    else:
                        right -= 1
        return ans
            