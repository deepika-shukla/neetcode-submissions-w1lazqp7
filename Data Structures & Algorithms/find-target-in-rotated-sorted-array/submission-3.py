class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l+r)//2

            #check if target is in mid position
            if target == arr[mid]:
                return mid
            
            #check for left sorted array
            if arr[l] <= arr[mid]:
                #now the condition taget does not exist within this range
                if arr[l] > target or arr[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            elif arr[mid] < arr[r]:
                if arr[mid] > target or arr[r] < target:
                    r = mid-1
                else:
                    l = mid+1
        return -1

    