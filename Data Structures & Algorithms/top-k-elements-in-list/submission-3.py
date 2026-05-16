class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # nums.sort(reverse=True)
        # s = []
        # for i in nums:
        #     if i not in s:
        #         s.append(i)
        #         if len(s) == k:
        #             return s

        count = [[] for i in range(len(nums)+1)]

        count_d = {}
        for i in nums:
            count_d[i] = 1 + count_d.get(i, 0)
        
        for key,v in count_d.items():
            count[v].append(key)
        ans = []
        for i in range(len(count) -1, -1, -1):
            for j in count[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans


