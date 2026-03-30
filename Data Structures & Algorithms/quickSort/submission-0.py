# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def quickSortHelper(self, pairs, s, e):
        #edge case when only one or no element
        if e-s+1 <= 1:
            return pairs
        
        #take pivot element as last
        pivot = pairs[e]
        
        #take start of index
        left = s

        #now we have to get smaller elements at left
        for i in range(s,e):
            if pairs[i].key < pivot.key:
                #then swap the element from left and currently on i
                pairs[i], pairs[left] = pairs[left], pairs[i]
                #increase the left pointer
                left += 1
        
        #once all elements are swapped, we need to bring pivot
        # element at correct position
        pairs[e] = pairs[left] # the large element we send at last
        pairs[left] = pivot # pivot came at the position where at left aall smaller elements and on the right all the greater elements

        #now divide the array from pivot index which is left
        self.quickSortHelper(pairs, s, left-1)
        self.quickSortHelper(pairs, left+1,e)


    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs