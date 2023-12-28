class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        for i, ns in enumerate(graph):
            if i not in visited:
                q = deque([i])
                visited[i] = 0
                # for n in ns:
                    # q.append(n)
                    # visited[n] = 1
                while q:
                    cur = q.pop()
                    for nb in graph[cur]:
                        if nb not in visited:
                            q.append(nb)
                            visited[nb] = 1 - visited[cur]
                        elif visited[nb] == visited[cur]:
                            return False
        return True
