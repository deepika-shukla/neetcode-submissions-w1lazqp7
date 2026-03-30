class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #insertion sort

        for j in range(1, len(nums)):
            i = j - 1
            num = nums[j]

            while i >= 0 and nums[i] > num:
                nums[i+1] = nums[i]
                i -= 1

            nums[i+1] = num
        return nums