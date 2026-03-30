class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #we have create target using the triplets
        #if any triplet the number is  higher than target we can ignore it
        #for all other we will check if for other index we are getting the same value
        #as target we can return true

        #set to keep track we found all position
        found = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                #we can ignore
                continue
            
            for i in range(len(t)):
                if t[i] == target[i]:
                    found.add(i) #add that index where we found the same val as target
        
        # if len == 3 means we found for all index and we can get the target
        return len(found) == 3
