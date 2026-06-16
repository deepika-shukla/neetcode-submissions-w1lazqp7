class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:\
        # greedy approach
        intervals.sort(key = lambda k : k[0])
        count = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                # no overlap
                prevEnd = end
            else:
                count += 1
                prevEnd = min(prevEnd, end)
        return count



