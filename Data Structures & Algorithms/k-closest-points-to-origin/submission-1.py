class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = {} #distance : values

        for x1,y1 in points:
            distance = pow((x1**2 + y1**2), 0.5)
            if distance in d:
                d[distance].append((x1,y1))
            else:
                d[distance] = [(x1,y1)]
        l = list(d.keys())
        heapq.heapify(l)
        ans = []
        for i in range(len(d)):
            distance = heapq.heappop(l)
            for coord in d[distance]:
                if len(ans) == k:
                    return ans
                ans.append(coord)
        return ans



