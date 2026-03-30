class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        k = set()

        for i in nums:
            if i in k:
                return i
            else:
                k.add(i)
        

        