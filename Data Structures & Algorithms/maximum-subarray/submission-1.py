class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """We have to find the largest subarray sum
        Now we don't want negative sum so we will ignore it
        And keep track of larget sum"""

        curr = 0 #which will store all the current sum
        final = -9999 #the largest sum we will have

        for i in nums:
            #check if current sum is < 0 then make it 0
            if curr < 0:
                curr = 0

            #add the number to current sum
            curr += i

            #check if current is larget
            if final < curr:
                final = curr
        return final
            
            

         
            
        