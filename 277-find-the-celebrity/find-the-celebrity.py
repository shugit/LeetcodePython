# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = deque([x for x in range(n)]) 
        while len(candidate) >=2 :
            p1 = candidate.popleft()
            p2 = candidate.popleft()
            if knows(p1, p2) and not knows(p2, p1):
                candidate.append(p2)
            else:
                candidate.append(p1)
        p = candidate.popleft()
        for i in range(n):
            if i == p:
                continue
            if not knows(i, p) or knows(p, i):
                return -1
        return p
