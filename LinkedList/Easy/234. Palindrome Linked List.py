class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        for i in range(len(lst) // 2):
            if lst[i] != lst[-i - 1]:
                return False
        return True