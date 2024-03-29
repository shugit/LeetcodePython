# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def serial(node):
            if not node:
                return "N"
            return f"{node.val},{serial(node.left)},{serial(node.right)}"
        res = serial(root)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deser():
            val = node_list.popleft()
            if val == "N":
                return None
            node = TreeNode(val)
            node.left = deser()
            node.right = deser()
            return node
        node_list = deque(data.split(","))
        return deser()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))