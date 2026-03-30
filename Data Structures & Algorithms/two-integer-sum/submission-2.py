class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # in this we need to find the pair whose sum is equal to target
        # we can do either in O(n^2) by iterating twice and adding
        # numbers together till we get the answer
        # or we can do in O(n) in such a way, we know the pair exist
        # we can create a dictionary to enter the numbers and their
        # indices and traverse through the array if the diff is present
        # in the dictionary, we found the pair

        dictionary = {} # number : index

        for i in range(len(nums)):
            #calculate the difference
            diff = target - nums[i]

            #check if the diff is present in dictionary
            if diff in dictionary:
                # we found the pair
                # return dictionary[i] first as it occur first
                return [dictionary[diff], i]
            
            #otherwise add the number and index in dictionary
            dictionary[nums[i]] = i