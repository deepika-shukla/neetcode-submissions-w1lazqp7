class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        # we will keep track of all min numbers
        # using min heap
        minheap = list(count.keys())
        heapq.heapify(minheap)

        # till we have minheap we will form groups
        while minheap:
            smallest = minheap[0]

            # then find its next consecutives
            for i in range(smallest, smallest+groupSize):
                if i not in count:
                    return False
                # if its exist decrease the count
                count[i] -= 1
                if count[i] == 0:
                    # we need to pop from minheap
                    # but if the popped element is not smallest
                    # then we cannot complete group
                    # we can return false
                    if i != minheap[0]:
                        return False
                    # if it is smallest then pop
                    heapq.heappop(minheap)
        return True

        
        