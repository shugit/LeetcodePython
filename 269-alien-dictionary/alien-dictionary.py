class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(set)
        in_degree = Counter({c:0 for w in words for c in w})
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in g[c1]:
                        g[c1].add(c2)
                        in_degree[c2] += 1
                    break
            else:
                if len(w2) < len(w1):
                    return ""
        res = []
        q = deque()
        # print(g)
        # print(in_degree)
        for node, count in in_degree.items():
            print(node,count)
            if count == 0:
                q.append(node)
        while q:
            node = q.popleft()
            res.append(node)
            for nei in g[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        # print(res)
        if len(res) < len(in_degree):
            return ""
        return "".join(res)


