class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums)+1)]

        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        for key, v in count.items():
            arr[v].append(key)
        
        ans = []
        for i in range(len(arr)-1,-1,-1):
            if len(ans) == k:
                return ans
            for j in arr[i]:   
                ans.append(j)

