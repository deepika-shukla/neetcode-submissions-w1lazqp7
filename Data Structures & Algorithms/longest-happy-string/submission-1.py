class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # we will use heap to get the highest number of char
        # if two occurences are already completed we won't add 

        maxheap, res = [], ""

        for c, char in [[-a, "a"], [-b, "b"], [-c, "c"]]:
            if c != 0:
                heapq.heappush(maxheap, [c, char])
        
        while maxheap:
            # pop from heap
            c, char = heapq.heappop(maxheap)

            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxheap:
                    break
                # we can't add the char, we have to add next frequent
                c2, char2 = heapq.heappop(maxheap)
                res += char2 # include in res
                c2 += 1 # increase the count
                # add this back as well in heap
                if c2 != 0:
                    heapq.heappush(maxheap, [c2, char2])
            else:
                res += char
                c += 1

            # now we need to add back to heap, if that char still exist with count > 1
            if c != 0:
                heapq.heappush(maxheap, [c, char])
        return res