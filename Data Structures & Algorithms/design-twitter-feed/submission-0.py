class Twitter:

    def __init__(self):
        # we will keep three parameters
        self.count =0 # this will tell the recent tweet
        self.tweetmap = defaultdict(list) # userid -> [count,tweetid]
        self.followmap = defaultdict(set) # followerid -> (set of followeeid)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1 # we need negative for maxHeap implementation

    def getNewsFeed(self, userid: int) -> List[int]:
        # now to get latets tweet we will keep track of heap
        res = [] # ans
        minheap = []
        
        # for edge case as user itself as followid
        self.followmap[userid].add(userid)
        for followeeid in self.followmap[userid]:
            # check if the followeeid has created any tweet
            if followeeid in self.tweetmap:
                # get the last index
                index = len(self.tweetmap[followeeid]) - 1
                # get the count and tweetid from that index
                count, tweetid = self.tweetmap[followeeid][index]
                # in heap we will add the tweetid
                heapq.heappush(minheap, [count, tweetid, followeeid ,index-1] )
        
        # first heapify the heap
        heapq.heapify(minheap)

        # now we need to get the top 10 tweets
        while minheap and len(res) < 10:
            # get the latest tweet
            count, tweetid, followeeid, index = heapq.heappop(minheap)
            res.append(tweetid)
            # now for that followid, we can have multiple tweets
            # add that in heap if any of them is latest
            if index >= 0:
                count, tweetid = self.tweetmap[followeeid][index]
                heapq.heappush(minheap, [count, tweetid, followeeid, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        
