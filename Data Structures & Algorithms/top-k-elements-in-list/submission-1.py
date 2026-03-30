class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums)+1)]
        d = {}

        for i in nums:
            d[i] = 1 + d.get(i,0)
        
        for i,v in d.items():
            count[v].append(i)
        print(count)

        ans = []
        for i in range(len(count) - 1, -1, -1):
            if count[i]:
                for j in count[i]:
                    ans.append(j)
                    if len(ans) == k:
                        return ans
             




        