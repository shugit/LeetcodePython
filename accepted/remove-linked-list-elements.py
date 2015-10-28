# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    #remove this will speed up
    def __repr__(self):
        next_node = self.next
        str = '%r'%(self.val)
        while next_node is not None:
            str += ' %r'%(next_node.val)
            next_node = next_node.next
        return str

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head is None:
            return None
        while head.val == val:
            if head.next is not None:
                head = head.next
            else:
                return None
        pre = head
        next = pre.next
        while next is not None:
            #print 'next is %d'%(next.val)
            if next.val == val:
                pre.next = next.next
                next = pre.next
            else:
                pre = next
                next = pre.next
        return head



s = Solution()
l = ListNode(5)
l.next = ListNode(5)
l.next.next = ListNode(3)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next = ListNode(3)
l.next.next.next.next.next.next.next = ListNode(7)
l.next.next.next.next.next.next.next.next = ListNode(8)
l.next.next.next.next.next.next.next.next.next = ListNode(9)
l.next.next.next.next.next.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next.next.next.next.next.next = ListNode(5)

#print l
print s.removeElements(ListNode(1),1)