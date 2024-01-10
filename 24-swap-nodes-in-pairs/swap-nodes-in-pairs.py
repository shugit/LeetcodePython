class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(node):
            if not node or not node.next:
                return node
            p = swap(node.next.next)
            nextNode = node.next
            node.next.next = node
            node.next = p
            return nextNode
        return swap(head)