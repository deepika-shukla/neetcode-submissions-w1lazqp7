class Solution:
    def topKFrequent(self, nums: List[int], target: int) -> List[int]:
        ans = [[] for i in range(len(nums)+1)]
        
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for k,v in count.items():
            ans[v].append(k)
        
        res = []
        for i in range(len(ans)-1,-1,-1):
            list1 = ans[i]
            for j in range(len(list1)-1,-1,-1):
                res.append(list1[j])
                if len(res) == target:
                    return res
                