class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # tickets.sort()
        g = defaultdict(list)
        for f, t in tickets:
            g[f].append(t)
        for _, neibors in g.items():
            neibors.sort(reverse=True)

        def dfs(root):
            neibors = g[root]
            while neibors:
                nextNode = neibors.pop()
                dfs(nextNode)
            res.append(root)
        res = []
        dfs("JFK")
        return reversed(res)