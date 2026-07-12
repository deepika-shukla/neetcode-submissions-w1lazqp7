class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]

            if ans[-1][1] >= start:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])
        return ans
