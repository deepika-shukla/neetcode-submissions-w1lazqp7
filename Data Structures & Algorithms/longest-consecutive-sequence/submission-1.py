class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we have to find the consecutive sequence
        # we will look for the start of sequence, i.e the previous of it does not exist
        # once we find the start we will check its consecutive seqence
        # and manage the maximum 
        # if not start contiue to next

        max_s = 0

        for i in nums:
            count = 1 
            #check for start
            curr = i
            if (curr-1) not in nums:
                while curr+1 in nums: #5
                    count += 1#4
                    curr += 1#6
                if max_s < count:
                    max_s = count
        return max_s
                    


