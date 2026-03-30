class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set()
        for i in nums:
            if i in n:
                return True
            n.add(i)
        return False
        