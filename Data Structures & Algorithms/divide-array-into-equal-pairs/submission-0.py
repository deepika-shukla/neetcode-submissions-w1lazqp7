class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        for k,v in count.items():
            if v % 2 != 0:
                return False
        return True
