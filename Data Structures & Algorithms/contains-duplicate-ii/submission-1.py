class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = {}

        for r in range(len(nums)):
            if nums[r] in hashset:
                if abs(r-hashset[nums[r]]) <= k:
                    return True
            hashset[nums[r]] = r
        return False
