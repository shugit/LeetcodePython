class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        return self.sol2(head)
    def sol2(self, head):
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        cur = head
        while cur:
            lastNode = stack.pop()
            nextNode = cur.next
            if lastNode == nextNode or lastNode.next == nextNode:
                lastNode.next = None
                break
            cur.next = lastNode
            lastNode.next = nextNode
            cur = cur.next.next
        return

    def sol1(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        left = head
        right = head.next
        while right and right.next:
            left = left.next
            right = right.next.next
        mid = left.next
        left.next = None
        prev = None
        while mid:
            tmp = mid.next
            mid.next = prev
            prev = mid
            mid = tmp
        second = prev
        first = head
        while second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
