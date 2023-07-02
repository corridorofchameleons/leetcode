class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        cur = head
        leng = 1
        while cur.next:
            leng += 1
            cur = cur.next

        rev_its = leng - (k % leng)

        cur.next = head
        cur = head

        for i in range(rev_its):
            cur = cur.next

        head = cur

        for i in range(leng - 1):
            cur = cur.next

        cur.next = None

        return head