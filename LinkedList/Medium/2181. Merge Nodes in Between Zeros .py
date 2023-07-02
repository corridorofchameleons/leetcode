class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        head = head.next
        counter = 0
        while head:
            counter += head.val
            if head.val == 0:
                nodes.append(ListNode(counter))
                counter = 0
            head = head.next

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        return nodes[0]