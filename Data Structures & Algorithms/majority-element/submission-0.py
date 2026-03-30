class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        m = max(count.values())

        for k,v in count.items():
            if v == m:
                return k