class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0] * len(graph) # 1 for odd, -1 for even
        def bfs(root):
            if odd[root]:
                return True
            odd[root] = 1
            q = deque([root])
            while q:
                i = q.popleft()
                for nei in graph[i]:
                    if odd[i] == odd[nei]:
                        return False
                    if not odd[nei]:
                        odd[nei] = -odd[i]
                        q.append(nei)
            return True
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True