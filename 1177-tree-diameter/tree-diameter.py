class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for s, e in edges:
            adj[s].add(e)
            adj[e].add(s)
        counter = 0 
        toRemove = []
        while len(adj) > 2: 
            for u in adj: 
                if len(adj[u]) == 1: 
                    toRemove.append(u)
            for u in toRemove: 
                v = adj[u].pop()
                adj.pop(u)
                adj[v].remove(u)
            toRemove = []
            counter += 2
            
        return counter + 1 if len(adj) == 2 else counter 
