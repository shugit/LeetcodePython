# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre, post):
            if not pre or not post:
                return None
            node = TreeNode(pre[0])
            post.pop()
            if len(pre) == 1:
                return node
            leftVal = pre[1]
            left_cnt = post.index(leftVal) + 1
            node.left = dfs(pre[1:left_cnt + 1],post[0:left_cnt])
            node.right = dfs(pre[left_cnt + 1:], post[left_cnt:])
            return node
        return dfs(preorder, postorder)