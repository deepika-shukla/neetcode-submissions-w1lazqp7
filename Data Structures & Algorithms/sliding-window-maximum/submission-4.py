class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Bruteforce

        max_array = []

        i = 0
        while i+k-1 < len(nums):
            m = -9999999999999999
            for j in range(i, i+k):
                if nums[j] > m:
                    m = nums[j]
            max_array.append(m)
            i += 1
        return max_array
        

