class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # we need to merge the elements of both array into 1
        # and also last m elemnets in nums1 is 0 which we can replace
        # with higher elements as total lenth is m+n

        # therefroe we will start with last
        last = m + n -1
        i = m -1
        j = n - 1

        while j >=0:

            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -=1
            
            last -=1