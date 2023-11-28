# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(curr):
            if not curr:
                return curr
            if key < curr.val:
                curr.left = delete(curr.left)
                return curr
            elif key > curr.val:
                curr.right = delete(curr.right)
                return curr
            else: 
                if not curr.left:
                    return curr.right
                elif not curr.right:
                    return curr.left
                else:
                    node = curr.right
                    while node.left:
                        node = node.left
                    node.left = curr.left
                    return curr.right
        return delete(root)
