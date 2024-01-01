# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sol2(head)

    def sol1(self, head):
        if not head:
            return None
        q = []
        cur = head
        while cur:
            q.append([cur.val, cur])
            cur = cur.next
        q.sort(key=lambda x: x[0])
        for i in range(1, len(q)):
            q[i-1][1].next = q[i][1]
        q[len(q)-1][1].next = None
        return q[0][1]

    def sol2(self, head):
        def mergeSort(node):
            # print(node)
            if not node or not node.next:
                return node
            slow, fast = node, node.next
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            mid = slow.next
            slow.next = None
            left = mergeSort(node)
            right = mergeSort(mid)
            # print(left, right)
            dummy = ListNode(0)
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            curr.next = left or right
            return dummy.next
        return mergeSort(head)
        