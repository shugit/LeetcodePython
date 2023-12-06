class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            graph[i].append(j)
        # print(graph)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if graph[node] == []:
                return True
            visited.add(node)
            for i in graph[node]:
                res = dfs(i)
                if not res:
                    return False
            visited.remove(node)
            graph[node] = []
            return True
        for i in range(len(graph)):
            # print("start with",i)
            res = dfs(i)
            if not res:
                return False
        return True