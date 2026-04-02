class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for i in arr:
            freq[i] = 1 + freq.get(i, 0)
        print(freq)
        ans = -1 
        for k, v in freq.items():
            if k==v and ans < k:
                ans = k
        return ans