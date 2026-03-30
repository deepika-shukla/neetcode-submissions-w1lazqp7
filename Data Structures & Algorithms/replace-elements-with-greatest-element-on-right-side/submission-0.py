class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        great = 0
        output = [-1]

        for i in range(len(arr)-1, 0, -1):
            if great < arr[i]: # 3
                great = arr[i]
            output.append(great)
        return output[::-1]

         