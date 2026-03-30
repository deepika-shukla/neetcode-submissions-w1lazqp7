class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Brute Force
        
        # # we can create dictionary to store all differences
        # diff = {} # difference : [keys]

        # for i in arr:
        #     d = abs(i - x)

        #     if d not in diff:
        #         diff[d] = []
        #     diff[d].append(i)
        # print(diff)

        # keys = list(diff.keys())
        # keys.sort()

        # ans = []
        # for i in keys:
        #     for v in diff[i]:
        #         ans.append(v)
        #         if len(ans) == k:
        #             return sorted(ans)


        # BINARY SEARCH
        l, r = 0, len(arr) - k

        while l < r:
            m = (l + r) // 2

            if x - arr[m] > arr[m+k] - x:
                # right window is correct
                l = m + 1
            else:
                # seach in left
                r = m
        return arr[l:l+k]
