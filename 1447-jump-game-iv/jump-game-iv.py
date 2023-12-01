class Solution:
    def minJumps(self, arr: List[int]) -> int:
        g = {}
        for i, a in  enumerate(arr):
            if a not in g:
                g[a] = []
            g[a].append(i)
        step = 0
        q = [0]
        visited = set([0])
        # visited.add(0)
        # print(g)
        while q:
            level = []
            for i in q:
                if i == len(arr) - 1:
                    return step
                if arr[i] in g:
                    for next_i in g[arr[i]]:
                        if next_i not in visited:
                            visited.add(next_i)
                            level.append(next_i)
                    del g[arr[i]]
                if i - 1 >= 0 and i-1 not in visited:
                    visited.add(i-1)
                    level.append(i-1)
                if i + 1 <= len(arr) - 1 and i+1 not in visited:
                    visited.add(i+1)
                    level.append(i+1)
            step += 1
            print(step, level)
            q = level
        return -1