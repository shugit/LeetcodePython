class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.recursive(head, n)
    def recursive(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head
        for _ in range(n):
            r = r.next
        if not r:
            return head.next
        while r.next:
            l, r = l.next, r.next
        l.next = l.next.next
        return head

    def iterative(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy
        for i in range(0,n):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head    
