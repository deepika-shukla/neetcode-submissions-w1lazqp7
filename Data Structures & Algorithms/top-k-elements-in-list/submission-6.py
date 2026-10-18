class Solution:
    def topKFrequent(self, nums: List[int], target: int) -> List[int]:
       
        ans = [[] for i in range(len(nums) + 1)]

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for k, v in count.items():
            ans[v].append(k)
        res =[]
        for i in range(len(ans)-1,-1,-1):
            l = ans[i]
            for n in l:
                res.append(n)
                if len(res) == target:
                    return res
                
        

