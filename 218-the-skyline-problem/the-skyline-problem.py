import heapq
class Point:
    def __init__(self,x,id,h,type):
        self.x = x
        self.id = id
        self.h = h
        self.type = type
        
    def __lt__(self, other):
        return self.x < other.x

    def __str__(self):
        return f"[{self.x},{self.h},{self.type},{self.id}]"
        
    def __repr__(self):
        return self.__str__()

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for b in buildings:
            points.append(Point(b[0],b[1],b[2],'i'))
            points.append(Point(b[1],b[0],b[2],'o'))
        points.sort()
        # print(points)
        q = []
        max_height = 0
        res = []
        def remove(q,p):
            for i in range(0, len(q)):
                if q[i].x == p.id and q[i].h == p.h and q[i].id == p.x:
                    # print(f"removed {i}:{q[i]}")
                    del q[i]
                    break
        i = 0
        while i < len(points):
            cur = points[i]
            local_height = max_height
            while i < len(points) and points[i].x == cur.x:
                p = points[i]
                if p.type == 'i': 
                    # print(f"i, {p}")
                    q.append(p)
                    local_height = max(local_height, p.h)
                if p.type == 'o': 
                    # print(f"o, {p}")
                    remove(q, p)
                    local_height = max([x.h for x in q]) if len(q) > 0 else 0
                i += 1
            if local_height != max_height:
                max_height = local_height
                res.append([cur.x, local_height])
        return res
            