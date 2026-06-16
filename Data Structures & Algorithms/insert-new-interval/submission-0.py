class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key= lambda k : k[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last = output[-1][1]
            if last >= start:
                output[-1][1] = max(end, last)
            else:
                output.append([start, end])
        return output
