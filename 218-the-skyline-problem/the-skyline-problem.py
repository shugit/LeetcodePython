import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        return self.sol2(buildings)
        points = []
        for i,b in enumerate(buildings):
            points.append([b[0],i,'i'])
            points.append([b[1],i,'o'])
        points.sort()
        q = []
        max_height = 0
        res = []
        def remove(q,p):#p:[b[1],i,'o']
            for i in range(0, len(q)):
                b1 = buildings[q[i][1]]
                b2 = buildings[p[1]]
                if b1[0] == b2[0] and b1[1] == b2[1] and b1[2] == b2[2]:
                    # print(f"removed {i}:{q[i]}")
                    del q[i]
                    break
        i = 0
        while i < len(points):
            cur = points[i]
            cur_x = points[i][0]
            local_height = max_height
            while i < len(points) and points[i][0] == cur[0] :
                p = points[i]
                b = buildings[p[1]]
                if p[2] == 'i': 
                    # print(f"i, {p}")
                    q.append(p)
                    local_height = max(local_height, b[2])
                if p[2] == 'o': 
                    # print(f"o, {p}")
                    remove(q, p)
                    local_height = max([buildings[x[1]][2] for x in q]) if len(q) > 0 else 0
                i += 1
            if local_height != max_height:
                max_height = local_height
                res.append([cur[0], local_height])
        return res

    def sol2(self, buildings: List[List[int]]) -> List[List[int]]:
        edges = []
        for i,b in enumerate(buildings):
            edges.append([b[0],i])
            edges.append([b[1],i])
        edges.sort()
        live = []
        res = []
        i = 0
        while i < len(edges):
            cur_x = edges[i][0]
            while i < len(edges) and edges[i][0] == cur_x :
                b_idx = edges[i][1]
                if buildings[b_idx][0] == cur_x: # check if this is left edge of building b_idx
                    right = buildings[b_idx][1]
                    height = buildings[b_idx][2]
                    heapq.heappush(live, [-height, right])
                while live and live[0][1] <= cur_x:
                    heapq.heappop(live)
                i += 1
            max_height = -live[0][0] if live else 0
            if not res or max_height != res[-1][1]:
                res.append([cur_x, max_height])
        return res
            