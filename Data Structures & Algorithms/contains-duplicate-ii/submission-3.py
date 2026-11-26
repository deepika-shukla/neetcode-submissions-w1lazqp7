class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        l,r = 0,0
        s = set()

        while r < len(nums):
            if r - l > k:
                s.remove(nums[l])
                l += 1
            if nums[r] in s:
                return True
            
            s.add(nums[r])
            
            r += 1
        return False