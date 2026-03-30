# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, arr, s, m, e):
        # divide the array in two parts
        L = arr[s:m+1]
        R = arr[m+1:e+1]

        #take three pointer, two for the part, and one for our main arr
        i = 0 
        j= 0
        k = s

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    
    def mergesortalogorithm(self, arr, s, e):
        #check if only one element and no element means already sorted
        if (e-s) + 1 <= 1:
            return arr
        
        m = (s+e)//2

        #now divide array into two parts
        self.mergesortalogorithm(arr, s, m)
        self.mergesortalogorithm(arr, m+1, e)

        #now merge the divided array in dorted manner
        self.merge(arr,s,m,e)

        #return teh final sorted array
        return arr



    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergesortalogorithm(pairs, 0, len(pairs)-1)
