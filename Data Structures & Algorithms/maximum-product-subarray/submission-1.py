class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minp = 1
        maxp = 1
        res = nums[0]
        
        #[1,2,-3,4]
        #we have to keep track of min and max

        for n in nums:
            temp = maxp*n
            maxp = max(n,n*maxp,n*minp)
            minp = min(temp,n*minp, n)

            res = max(res, maxp)
        return res

