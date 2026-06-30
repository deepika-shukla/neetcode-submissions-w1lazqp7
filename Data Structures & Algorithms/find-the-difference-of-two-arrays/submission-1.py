class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a1 = []
        a2 = []
        ans =[]

        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in a1:
                a1.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in a2:
                a2.append(nums2[i])
        ans.append(a1)
        ans.append(a2)
        return ans