class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ancestors = set()
        
        # 找到 p 的所有祖先节点
        while p:
            p_ancestors.add(p)
            p = p.parent
        
        # 查找第一个在 p 的祖先中出现的 q 的祖先节点
        while q not in p_ancestors:
            q = q.parent
        
        return q