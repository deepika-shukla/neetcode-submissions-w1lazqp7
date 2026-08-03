class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = [[] for i in range(len(nums)+1)] 

        d = {}
        for i in nums:
            d[i] = 1+d.get(i,0)
        
        for n,c in d.items():
            count[c].append(n)
        print(count)
        ans = []
        for i in range(len(count)):
            if count[i] != []:
                count[i].sort(reverse=True)
                for j in count[i]:
                    for _ in range(i):
                        ans.append(j)
        return ans
