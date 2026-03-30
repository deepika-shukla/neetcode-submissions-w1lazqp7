class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # we need to find the subarray with max product
        # since we have negative integers we need to keep
        # track of both minProd and maxProd since, two negative
        # can make larger product

        cur_min, cur_max = 1,1
        result = max(nums)

        for n in nums:

            # we need to take care for edge case when number is zero
            if n == 0:
                cur_min, cur_max = 1,1
                continue
            
            #our cur_max will change when computing, we will store in temp
            temp = cur_max*n 
            cur_max = max(n, n*cur_max, n*cur_min)
            cur_min = min(n, temp, n*cur_min)

            result = max(result, cur_max)
        
        return result



