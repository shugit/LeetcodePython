"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        node_list = []
        def convert(curr):
            if not curr:
               return
            convert(curr.left)
            node_list.append(curr)
            # print(curr.val)
            convert(curr.right)
        # print(node_list)
        convert(root)
        for i in range(0, len(node_list)):
            node_list[i].right = node_list[(i+1)%len(node_list)]
            node_list[i].left = node_list[i-1]
        return node_list[0]