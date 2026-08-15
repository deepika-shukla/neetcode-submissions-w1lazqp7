class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*(2 * len(nums))
        l = len(nums)
        for i in range(l):
            ans[i] = ans[i+l] = nums[i]
        return ans

        