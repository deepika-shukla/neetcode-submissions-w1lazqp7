class Solution:
    def search(self, arr: List[int], target: int) -> int:
        # # we need to find the target in rotated array
        # # if could have two possibility eitheer it is sorted part
        # # or it might exist in unsorted part

        # l = 0
        # r = len(arr) - 1

        # while l <= r:
        #     mid = (l+r)//2

        #     if arr[mid] == target:
        #         return mid

        #     if arr[l] <= arr[mid]:
        #         # not if target does not present between these
        #         # two values it will be on other side
        #         if target < arr[l] or target > arr[mid]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     else:
        #         if target < arr[mid] or target > arr[r]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        # return -1



        # we will have one sorted array either in left or right

        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l+r) // 2
            if arr[mid] == target:
                return mid

            # left sorted
            if arr[l] <= arr[mid]:
                if arr[l] <= target < arr[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            # right sorted
            else:
                if arr[mid] < target <= arr[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1



























