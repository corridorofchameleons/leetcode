class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        while head:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp

        return cur