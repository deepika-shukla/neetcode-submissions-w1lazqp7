class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)

        l1, l2 = 0,0
        new  = []
        mid = int(length/2)

        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] < nums2[l2]:
                new.append(nums1[l1])
                l1 += 1
            else:
                new.append(nums2[l2])
                l2 += 1
        
        while l1 < len(nums1):
            new.append(nums1[l1])
            l1 += 1

        while l2 < len(nums2):
            new.append(nums2[l2])
            l2 += 1
        
        if length % 2 == 0:
            return (new[mid-1] + new[mid])/2
        else: 
            return new[mid]
