class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        
        node = head
        while node.next != head:
            if node.val <= insertVal <= node.next.val:
                break
            elif node.val > node.next.val:
                if insertVal >= node.val or insertVal <= node.next.val:
                    break
            node = node.next
            
        new_node = Node(insertVal, node.next)
        node.next = new_node
        
        return head