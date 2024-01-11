class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        return self.sol_dfs(graph)
    def sol_dfs(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(node):
            for nei in graph[node]:
                if nei not in color:
                    color[nei] = -color[node]
                    if not dfs(nei):
                        return False
                else:
                    if color[nei] == color[node]:
                        return False
            return True

        for node, _ in enumerate(graph):
            if node not in color:
                color[node] = 1
                if not dfs(node):
                    return False
        return True
            




    def sol_bfs(self, graph: List[List[int]]) -> bool:
        visited = {}
        for i, ns in enumerate(graph):
            if i not in visited:
                q = [i]
                visited[i] = 0
                while q:
                    cur = q.pop()
                    for nb in graph[cur]:
                        if nb not in visited:
                            q.append(nb)
                            visited[nb] = 1 - visited[cur]
                        elif visited[nb] == visited[cur]:
                            return False
        return True
