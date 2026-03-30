class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        
        l = []
        for k,v in d.items():
            if v > len(nums) // 3:
                l.append(k)
        return l