# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        nodes = []
        def find(cur, curSum):
            nodes.append(cur.val)
            if not cur.left and not cur.right:
                if cur.val + curSum == targetSum:
                    res.append(nodes.copy())
            else:
                if cur.left:
                    find(cur.left, curSum + cur.val)
                if cur.right:
                    find(cur.right, curSum + cur.val)
            nodes.pop()
            
        find(root, 0)
        return res