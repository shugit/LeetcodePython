class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        return self.sol2(head)

    def sol2(self,head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        stack = []
        res = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            res[i] = stack[-1] if stack else 0
            stack.append(arr[i])
        return res


    def sol1(self, head):
        node = head
        stack = []
        res = []
        i = 0
        while node:
            res.append(0)
            while stack and stack[-1][1] < node.val:
                prev_i, prev = stack.pop()
                res[prev_i] = node.val
            stack.append([i, node.val])
            node = node.next
            i += 1
        return res