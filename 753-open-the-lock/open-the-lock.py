class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque(["0000"])
        visited = set()
        visited.add("0000")
        deadset = set(deadends)
        if "0000" in deadset:
            return -1
        step = -1
        while q:
            step += 1
            for i in range(0, len(q)):
                node = q.popleft()
                if node == target:
                    return step
                for j in range(0, 4):
                    # print(j, node)
                    n1 = node[:j] + str((int(node[j]) + 1) % 10) + node[j+1:]
                    if n1 not in visited and n1 not in deadset:
                        q.append(n1)
                        visited.add(n1)
                    n2 = node[:j] + str((int(node[j]) -1) % 10) + node[j+1:]
                    if n2 not in visited and n2 not in deadset:
                        q.append(n2)
                        visited.add(n2)
        return -1
            
                
                