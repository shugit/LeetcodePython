class Twitter:

    def __init__(self):
        self.f = defaultdict(set)
        # self.t = defaultdict(deque)
        self.t = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.f[userId].add(userId)
        self.t.appendleft([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        arr = []
        for uid, tid in self.t:
            if len(arr) == 10:
                break
            if uid in self.f[userId]:
                arr.append(tid)
        return arr


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