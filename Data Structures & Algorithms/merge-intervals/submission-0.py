class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #we want to merge the interval
        i = 0
        
        while i < len(intervals):
            j = i  +1
            swap = False
            while j < len(intervals):
                a = intervals[i] 
                b = intervals[j]

                if a[0] <= b[1] <= a[1]: 
                    intervals[j] = [min(a[0], b[0]), a[1]]
                    intervals.pop(i)
                    swap = True
                elif b[0] <= a[1] <= b[1]: 
                    intervals[j] = [min(a[0], b[0]), b[1]]
                    intervals.pop(i)
                    swap = True
                j += 1
            if not swap:
                i += 1
        return intervals
        
            


