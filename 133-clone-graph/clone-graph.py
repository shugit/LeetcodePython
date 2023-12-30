"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.twoPass(node)

    def onePass(self,node):
        if node is None:
            return None
        h = {}
        def dfs(node):
            if node in h:
                return h[node]
            copy = Node(node.val)
            h[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)

    def twoPass(self,node):
        if node is None:
            return None
        h = {}
        def dfs(node):
            h[node] = Node(node.val, node.neighbors)
            for nei in node.neighbors:
                if nei not in h:
                    dfs(nei)
        dfs(node)
        # print([v.val for k,v in h.items()])
        for origin,copy in h.items():
            copy.neighbors = []
            for nei in origin.neighbors:
                copy.neighbors.append(h[nei])
        return h[node]
