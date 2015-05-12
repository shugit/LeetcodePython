# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    val = None
    left = None
    right = None
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        return same(p,q)

def same(p,q):
    if p is None and q is None:
        print 'both none'
        return True
    elif p is None:
        print 'p is none, q is %d'%q.val
        return False
    elif q is None:
        print 'q is none, p is %d'%p.val
        return False
    else:
        print 'p=%d q=%d'%(p.val,q.val)
        if p.val!=q.val:
            return False
        return same(p.left,q.left) and same(p.right,q.right)


s = Solution()
p = TreeNode(1)
q = TreeNode(1)
q.left = TreeNode(4)
p.left = TreeNode(4)
q.left.right = TreeNode(5)
p.left.right = TreeNode(5)
print s.isSameTree(p,q)


