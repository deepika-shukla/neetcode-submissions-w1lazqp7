class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_arr = [0]*3

        for n in nums:
            count_arr[n] = count_arr[n]+ 1
        print(count_arr)
        k = 0
        for i in range(3):
            for c in range(count_arr[i]):
                nums[k] = i
                k += 1
        


        

        