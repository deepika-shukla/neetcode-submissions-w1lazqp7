class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Brute Force
        
        # we can create dictionary to store all differences
        diff = {} # difference : [keys]

        for i in arr:
            d = abs(i - x)

            if d not in diff:
                diff[d] = []
            diff[d].append(i)
        print(diff)

        keys = list(diff.keys())
        keys.sort()

        ans = []
        for i in keys:
            for v in diff[i]:
                ans.append(v)
                if len(ans) == k:
                    return sorted(ans)