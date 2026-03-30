class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l+r)//2
            
            if target == arr[m]:
                return m
            
            elif arr[l] <= arr[m]:
                if arr[l] > target or arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
                
            elif arr[m] < arr[r]:
                if arr[m] > target or arr[r] < target:
                    r = m - 1
                else:
                    l = m + 1
        return -1