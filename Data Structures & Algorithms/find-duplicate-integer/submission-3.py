class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # k = set()

        # for i in nums:
        #     if i in k:
        #         return i
        #     else:
        #         k.add(i)

        slow, fast = 0,0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # we get the poisition which two numbers are pointing
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        

        