class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        visited = set()
        g = defaultdict(set) #g[stop] = {bus_id}
        for i, stops in enumerate(routes):
            for stop in stops:
                g[stop].add(i)
        q = deque([(source, 0)])
        visited_routes, visited_stops = set(), set([source])
        while q:
            stop, res = q.popleft()
            if stop == target:
                return res
            for idx in g[stop]:
                if idx not in visited_routes:
                    visited_routes.add(idx)
                    for stop in routes[idx]:
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            q.append((stop, res+1))
        return -1
