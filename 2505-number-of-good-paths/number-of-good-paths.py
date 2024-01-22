class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        parent = [x for x in range(len(vals))]
        rank = [0] * len(vals)
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        def union_set(x,y):
            p1 = find(x)
            p2 = find(y)
            if p1 == p2:
                return
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                parent[p2] = p1
                rank[p1] += 1

        adj = defaultdict(set)
        for (f,t) in edges:
            adj[f].add(t)
            adj[t].add(f)
        values = defaultdict(set)
        for i, val in enumerate(vals):
            values[val].add(i)
        res = 0
        for val, nodes in sorted(values.items()):
            # print(val, nodes)
            for node in nodes:
                for neibor in adj[node]:
                    if vals[node] >= vals[neibor]:
                        union_set(node, neibor)
            # print(parent)
            group = {}
            for node in nodes:
                group[find(node)] = group.get(find(node), 0) + 1
            for size in group.values():
                res += (size * (size+1))//2
        return res