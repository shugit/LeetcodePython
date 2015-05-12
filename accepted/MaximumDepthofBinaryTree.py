# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find(root):
    if root is None:
        return 0
    else:
        left_depth = find(root.left)
        right_depth = find(root.right)
        return left_depth+1 if left_depth>=right_depth else right_depth+1

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        return find(root)



s = Solution()
t = TreeNode(3)
t.left = TreeNode(4)
t.left.left = TreeNode(5)
t.left.left.left = TreeNode(6)
t.right = TreeNode(7)
print s.maxDepth(t)