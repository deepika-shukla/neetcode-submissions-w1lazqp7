# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        length = len(pairs)
        output = []

        for i in range(1, length):
            cur = pairs[i]
            j = i - 1
            output.append(pairs[:])
            while j >= 0 and pairs[j].key > cur.key:
                pairs[j+1] = pairs[j]
                j-=1
            
            pairs[j+1] = cur
            # output.append(pairs[:])
        output.append(pairs[:])
        return output 