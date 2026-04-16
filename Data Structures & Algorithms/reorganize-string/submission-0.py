class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for i in s:
            count[i] = 1 + count.get(i, 0)

        maxheap = [[-cnt, char] for char, cnt in count.items()]
        # make it heap
        heapq.heapify(maxheap)

        prev= None # to check we don't take same charatcter twice
        res = ""
        #a=1, b=1, c= 1
        while maxheap or prev:
            # if prev is there but not maxheap
            # then no solution is possible
            if prev and not maxheap:
                return ""
            
            cnt, char = heapq.heappop(maxheap)
            res += char
            cnt += 1
            
            # if prev already exist update it
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if cnt !=0:
                prev = [cnt,  char]
        return res
