class Twitter:

    def __init__(self):
        self.f = defaultdict(set)
        # self.t = defaultdict(deque)
        self.t = defaultdict(deque)
        self.c = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t[userId].appendleft([self.c, tweetId])
        self.c += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.f[userId].add(userId)
        arr = []
        for fId in self.f[userId]:
            for i in range(0, min(10, len(self.t[fId]))):
                ts, tId = self.t[fId][i]
                arr.append((-ts, tId))
        heapq.heapify(arr)
        res = []
        for i in range(0, min(10, len(arr))):
            res.append(heapq.heappop(arr)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.f[followerId]:
            self.f[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)