class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.kahn(numCourses,prerequisites)

    def kahn(self, numCourses: int, prerequisites: List[List[int]]):
        indegrees = {u:0 for u in range(numCourses)}
        graph  = {u :[] for u in range(numCourses)}

        for dest,src in prerequisites:
            graph[src].append(dest)
            indegrees[dest] += 1
        q = deque()
        for a in indegrees:
            if indegrees[a] == 0:
                q.append(a)
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for nei in graph[u]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        return order if len(order) == numCourses else [] 