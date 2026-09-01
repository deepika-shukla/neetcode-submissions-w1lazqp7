class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1] * len(arr)
        largest = arr[-1]

        for i in range(len(arr) -2, -1,-1):
            if largest < arr[i]:
                ans[i] = largest
                largest = arr[i]
            else:
                ans[i] = largest
        return ans